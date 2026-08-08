<div align="center">

# 🛍️ LUCCI Frontend

### Frontend Application for the LUCCI Cloud Native E-Commerce Platform
<br/>

<div align="center">

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![AWS](https://img.shields.io/badge/Cloud-AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Jenkins](https://img.shields.io/badge/CI%2FCD-Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)](https://www.jenkins.io/)
[![Amazon S3](https://img.shields.io/badge/Storage-Amazon_S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)](https://aws.amazon.com/s3/)
[![CloudFront](https://img.shields.io/badge/CDN-CloudFront-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/cloudfront/)
[![Route53](https://img.shields.io/badge/DNS-Route_53-8C4FFF?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/route53/)

</div>

<br/>

> Built using **React + Node.js + Express + Docker + Amazon ECS Fargate**  
> Automated deployment with **Jenkins + Amazon ECR**  
> Frontend delivered through **Amazon S3 + CloudFront + Route 53**  
> Event-driven communication using **Amazon SQS**

</div>

----

# 🔍 Overview

This repository contains the frontend application for the LUCCI Cloud Native E-Commerce Platform.

It provides the customer-facing web interface while communicating with backend microservices through REST APIs.

The complete LUCCI platform consists of:

- Frontend
- User Service
- Product Service
- Order Service
- Payment Service
----

# 📦 Project Repositories

| Repository | Description |
|------------|-------------|
| **https://github.com/rozanaim2026/frontend-aws-devops.git** | React Application |
| **https://github.com/rozanaim2026/user-service.git** | User Authentication & Profile |
| **https://github.com/rozanaim2026/product-service.git** | Product Catalog |
| **https://github.com/rozanaim2026/order-service.git** | Order Management |
| **https://github.com/rozanaim2026/payment-service.git** | Razorpay Integration |

----

<div align="center">
  
# 🏗️ Architecture

  
  <p align="center">
  <img src="./assets/lucci-architecture.png" width="90%">
</p>

</div>

### Architecture Flow

```
Developer
      │
GitHub
      │
Webhook
      ▼
Jenkins
      │
Build Frontend
      │
Deploy Static Files
      ▼
Amazon S3
      │
CloudFront
      │
Route53
      │
Users
      │
REST API
      ▼
Application Load Balancer
      │
Backend Microservices
```

---

### Request Flow

1. The user accesses the application through **Route 53**.

2. Static React assets are served from **Amazon S3** via **CloudFront**.

3. API requests are routed through the **Application Load Balancer**.

4. The ALB forwards requests to the appropriate **ECS Fargate microservice**.

5. Services communicate with **Amazon RDS MySQL** for persistent storage.

6. Payment events are published to **Amazon SQS**, allowing the Order Service to process them asynchronously.

7. Docker images are automatically built by Jenkins and deployed to ECS through Amazon ECR.

---


## ✨ Features

- Responsive React Frontend
- Product Browsing
- Category Filtering
- Shopping Cart
- Cloud-native Deployment

----
# 🛠️ Tech Stack

| Category | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | React.js | User Interface |
| **CI/CD** | Jenkins | Automated Build & Deployment |
| **Cloud Storage** | Amazon S3 | React Frontend Hosting |
| **Content Delivery** | Amazon CloudFront | CDN |
| **DNS** | Amazon Route 53 | Domain Management |
| **SSL** | AWS Certificate Manager | HTTPS Certificates |
| **Version Control** | Git & GitHub | Source Code Management |

---

# ☁️ AWS Infrastructure

The application is deployed using a secure AWS architecture that separates public-facing resources from backend services running inside a private network.

| AWS Service | Purpose |
|--------------|---------|
| **Amazon S3** | Hosts React Frontend |
| **Amazon CloudFront** | Global CDN |
| **Amazon Route53** | Domain & DNS Management |
| **AWS Certificate Manager** | HTTPS SSL Certificates |
| **Security Groups** | Firewall Rules |
| **IAM** | Secure Access Control |

---


LUCCI follows a fully automated CI/CD pipeline.

```
Developer
     │
 Git Push
     ▼
GitHub Repository
     │
Webhook
     ▼
Jenkins Pipeline
     │
Checkout Source Code
     │
Push Images
     ▼
     │
Rolling Deployment
     ▼
     │
Production Environment
```

---

## ⚙️ Jenkins Pipeline Stages

| Stage | Purpose |
|--------|---------|
| Checkout Source | Clone Repository |
| Docker Build | Build Microservice Images |
| Push to ECR | Upload Images |
| ECS Deployment | Deploy Latest Containers |
| Verify Deployment | Health Checks |

---



# 📁 Frontend Repository Structure

| Folder / File | Description |
|---------------|-------------|
| `assets/` | Architecture diagram and application screenshots used in the documentation |
| `components/` | Reusable HTML components (Navbar, etc.) |
| `public/` | Static frontend assets |
| `src/` | JavaScript logic for frontend features |
| `index.html` | Landing page |
| `products.html` | Product listing page |
| `product-details.html` | Product details page |
| `collections.html` | Product collections |
| `cart.html` | Shopping cart |
| `checkout.html` | Checkout workflow |
| `orders.html` | User order history |
| `order-details.html` | Individual order details |
| `order-success.html` | Successful order confirmation |
| `wishlist.html` | Wishlist management |
| `profile.html` | User profile |
| `admin.html` | Admin dashboard |
| `style.css` | Global styling |
| `build.sh` | Frontend build script |
| `Jenkinsfile` | CI/CD pipeline |
| `package.json` | Project dependencies |


# Deployment 

Developer
      │
Git Push
      ▼
GitHub Repository
      │
Webhook
      ▼
Jenkins
      │
Build Frontend
      │
Deploy Static Files
      ▼
Amazon S3
      │
CloudFront
      │
Route 53
      ▼
Users
      │
REST API Calls
      ▼
Application Load Balancer

----
# 📸 Application Screenshots

## 🏠 Home Page

<p align="center">
  <img src="assets/HomePage.png" alt="Home Page" width="90%">
</p>

---

## 🛍️ Collections

<p align="center">
  <img src="assets/Collections.png" alt="Collections" width="90%">
</p>

---

## 👗 Women's Collection

<p align="center">
  <img src="assets/Womens.png" alt="Women's Collection" width="90%">
</p>

---

## 📦 Products

<p align="center">
  <img src="assets/Products.png" alt="Products" width="90%">
</p>

---

## 🛒 Checkout

<p align="center">
  <img src="assets/CheckoutPage.png" alt="Checkout Page" width="90%">
</p>

---

## 💳 Payment Process

<p align="center">
  <img src="assets/PaymentProcess.png" alt="Payment Process" width="90%">
</p>

---

## ✅ Payment Successful

<p align="center">
  <img src="assets/PaymentSuccessfull.png" alt="Payment Successful" width="90%">
</p>

----


# 🚀 Deployment

## Clone Repository

```bash
git clone https://github.com/rozanaim2026/frontend-aws-devops.git

cd frontend-aws-devops
```

---

# 📈 Future Improvements

- Progressive Web App (PWA)
- Responsive Design Enhancements
- Dark Mode
- Accessibility Improvements (WCAG)
- Image Optimization
- Lazy Loading
- Frontend Unit Testing
- Performance Optimization


---

# 👩‍💻 Author

<div align="center">

## Rozana IM

Cloud Engineer • DevOps Engineer • AWS Enthusiast

GitHub: https://github.com/rozanaim2026

LinkedIn: https://www.linkedin.com/in/rozana-im-a63541302/

</div>

---

# ⭐ Support

If you found this project helpful,

please consider giving it a ⭐ on GitHub.

It really helps and motivates me to build more cloud-native projects.

---

<div align="center">


## ☁️ Built with AWS • Docker • Jenkins • React • Node.js

### ❤️ Made with passion for Cloud & DevOps Engineering

</div>
