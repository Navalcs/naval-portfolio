import json, os, re, time, uuid
import boto3
from boto3.dynamodb.conditions import Key

table = boto3.resource("dynamodb").Table(os.environ.get("TABLE", "Leaderboard"))
MAX_SCORE = 2000  # simple anti-cheat cap


def resp(code, body):
    return {"statusCode": code, "headers": {"Content-Type": "application/json"}, "body": json.dumps(body)}


def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "")

    if method == "GET":
        r = table.query(KeyConditionExpression=Key("board").eq("main"), Limit=10)  # highest score first
        return resp(200, {"scores": [{"name": i["name"], "score": int(i["score"])} for i in r["Items"]]})

    if method == "POST":
        try:
            data = json.loads(event.get("body") or "{}")
            score = int(data.get("score"))
        except Exception:
            return resp(400, {"error": "bad request"})
        name = re.sub(r"[^\w ]", "", str(data.get("name", "Anon")))[:12].strip() or "Anon"
        if score < 0 or score > MAX_SCORE:
            return resp(400, {"error": "invalid score"})
        # zero-padded inverse score as sort key => ascending query returns best scores first
        sk = f"{MAX_SCORE - score:05d}#{int(time.time() * 1000)}#{uuid.uuid4().hex[:6]}"
        table.put_item(Item={"board": "main", "sk": sk, "name": name, "score": score})
        return resp(201, {"ok": True})

    return resp(405, {"error": "method not allowed"})
