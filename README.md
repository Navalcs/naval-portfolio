# ☁️ Naval Mohanraj — AWS Cloud Computing Portfolio

A responsive, interactive personal portfolio website built using HTML, CSS and JavaScript, hosted on **Amazon S3** and delivered globally through **Amazon CloudFront with HTTPS**.

The portfolio showcases my cloud computing journey, technical skills, projects, achievements and hands-on experience with AWS services. It also features two interactive games designed around cloud computing and cloud migration concepts.

## 🌐 Live Website

**Portfolio:** [View My Portfolio](d3njwbay4gsc7f.cloudfront.net)

**GitHub Repository:** [naval-portfolio](https://github.com/Navalcs/naval-portfolio)

## 📌 About the Project

I developed this portfolio to showcase my technical background, cloud computing knowledge and practical projects while pursuing my M.Sc. IT specialization in Cloud Computing.

The website focuses on presenting my skills and projects through an interactive and visually engaging interface rather than a traditional static portfolio.

A key objective was to understand how static websites can be deployed and delivered using AWS cloud infrastructure.

## ✨ Features

### 1. Personal Portfolio
- Introduction and professional profile.
- Educational background and career objectives.
- Technical skills with animated progress indicators.
- Project showcase with technology tags.
- GitHub, LinkedIn and email contact links.

### 2. Interactive UI
- Responsive layout for desktop and mobile devices.
- Glassmorphism-inspired card design.
- Animated gradient backgrounds and floating elements.
- Interactive navigation and smooth scrolling.
- Scroll progress indicator.
- Animated project cards and hover effects.
- Reduced-motion accessibility support.

### 3. Cloud Arcade — Interactive Game 🕹️

A hidden arcade game integrated into the portfolio.

- Catch stars and avoid downtime obstacles.
- Score tracking and multiple difficulty levels.
- Keyboard, mouse and touch controls.
- Sound effects with mute functionality.
- Personal information revealed through gameplay.
- Unlockable hidden project and AWS architecture explanation.
- Local high-score storage using browser localStorage.

### 4. Migrate It! — Cloud Migration Puzzle 🚚

An interactive learning game that demonstrates cloud migration concepts.

- Match on-premises infrastructure components with AWS services.
- Six migration challenges.
- Drag-and-drop and tap-to-match functionality.
- Tracks completion time and incorrect attempts.
- Includes explanations of the correct AWS service mappings.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| HTML5 | Website structure |
| CSS3 | Styling, animations and responsive layouts |
| JavaScript | Interactivity, dynamic rendering and game logic |
| Canvas API | Arcade game rendering |
| Google Fonts | Typography |
| Git & GitHub | Version control and source code management |
| Amazon S3 | Static website file storage |
| Amazon CloudFront | Content delivery and HTTPS distribution |

## ☁️ AWS Architecture

The portfolio is deployed using Amazon Web Services.

### Architecture Overview

**Visitor → Amazon CloudFront → Amazon S3**

1. **Amazon S3**
   - Stores the static website files.
   - Holds the HTML, CSS and JavaScript code.
   - Acts as the website's storage origin.

2. **Amazon CloudFront**
   - Delivers website content through a global Content Delivery Network (CDN).
   - Serves the website over HTTPS.
   - Uses CloudFront edge locations to improve content delivery.
   - Reduces repeated requests to the origin through caching.

### Architecture Diagram

```text
          Website Visitor
                 |
                 |
             HTTPS Request
                 |
                 v
        +-------------------+
        |   CloudFront      |
        |   Global CDN      |
        |   HTTPS Delivery  |
        +-------------------+
                 |
                 |
          Origin Request
                 |
                 v
        +-------------------+
        |    Amazon S3      |
        |  Static Website   |
        |  HTML / CSS / JS  |
        +-------------------+
                 |
                 v
          Website Content
```

## 📂 Project Structure

```text
naval-portfolio/
│
├── index.html
│
└── backend/
```

The current website implementation is contained in `index.html`, with its CSS and JavaScript embedded in the same file.

## 🚀 Deployment

The website is deployed using Amazon S3 and Amazon CloudFront.

### Deployment Workflow

1. Develop the website locally using HTML, CSS and JavaScript.
2. Push the latest source code to GitHub.
3. Upload the production website files to the Amazon S3 bucket.
4. Configure CloudFront to deliver content from the S3 origin.
5. Access the deployed website through the CloudFront HTTPS distribution URL.

### AWS Services Used

- Amazon S3 — Static website storage.
- Amazon CloudFront — CDN and HTTPS delivery.

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

- Hosting static websites on Amazon S3.
- Understanding the role of a CDN in website delivery.
- Configuring CloudFront for HTTPS delivery.
- Understanding the relationship between an origin server and edge locations.
- Working with Git and GitHub for version control.
- Understanding cloud hosting architecture.
- Building responsive and interactive web applications.

## 🔮 Future Improvements

- Automate deployments using GitHub Actions.
- Integrate a custom domain using Amazon Route 53.
- Improve website performance and caching configuration.
- Add website analytics and visitor tracking.
- Continue expanding cloud architecture demonstrations.

## 👨‍💻 Author

**Naval Mohanraj**

M.Sc. IT — Cloud Computing

Interested in AWS, Cloud Computing, Cloud Architecture and Cloud Migration.

- GitHub: [@Navalcs](https://github.com/Navalcs)
- LinkedIn: [Naval Mohanraj](https://linkedin.com/in/naval-mohanraj)
- Email: navalmohanraj07@gmail.com

---

⭐ If you find this project interesting, feel free to explore the repository and check out the live portfolio.

**Built with curiosity, creativity and AWS Cloud ☁️**
