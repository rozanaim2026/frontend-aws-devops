<div align="center">

# 🛍️ LUCCI — Cloud Native E-Commerce Platform

### **A production-grade microservices-based e-commerce platform deployed on AWS using modern DevOps practices**

<br/>

[![AWS](https://img.shields.io/badge/Cloud-AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Jenkins](https://img.shields.io/badge/CI%2FCD-Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)](https://www.jenkins.io/)
[![Amazon ECS](https://img.shields.io/badge/Compute-ECS_Fargate-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/ecs/)
[![Amazon ECR](https://img.shields.io/badge/Registry-Amazon_ECR-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/ecr/)
[![Amazon RDS](https://img.shields.io/badge/Database-Amazon_RDS-527FFF?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/rds/)
[![Amazon S3](https://img.shields.io/badge/Storage-Amazon_S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)](https://aws.amazon.com/s3/)
[![CloudFront](https://img.shields.io/badge/CDN-CloudFront-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/cloudfront/)
[![Route53](https://img.shields.io/badge/DNS-Route_53-8C4FFF?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/route53/)
[![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)

<br/>

> Built using **React + Node.js + Express + Docker + Amazon ECS Fargate**  
> Automated deployment with **Jenkins + Amazon ECR**  
> Frontend delivered through **Amazon S3 + CloudFront + Route 53**  
> Event-driven communication using **Amazon SQS**

</div>

----
# 🔍 Overview

LUCCI is a **production-style cloud-native e-commerce platform** designed using a **microservices architecture** and deployed entirely on **Amazon Web Services (AWS)**.

Instead of deploying a single monolithic application, LUCCI separates business functionality into multiple independent services that communicate securely while running inside **Amazon ECS Fargate**.

The project demonstrates real-world cloud engineering concepts including:

- Containerized microservices using Docker
- Automated CI/CD with Jenkins
- Image management using Amazon ECR
- Secure networking with Amazon VPC
- Public & Private Subnets
- Application Load Balancer
- Amazon RDS MySQL
- Amazon SQS asynchronous messaging
- HTTPS using AWS Certificate Manager
- Frontend hosting using Amazon S3
- Global content delivery using CloudFront
- DNS management using Route 53

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
Git Push
    ▼
GitHub
    │
Webhook
    ▼
Jenkins (EC2)
    │
Build Docker Image
    ▼
Amazon ECR
    │
Deploy Latest Image
    ▼
Amazon ECS Fargate
    │
Application Load Balancer
    │
────────────────────────────────────────
User Service
Product Service
Order Service
Payment Service
    │
Amazon RDS MySQL

Payment Service
      │
Amazon SQS
      │
Order Service

────────────────────────────────────────

User
 │
Route53
 │
CloudFront
 │
Amazon S3
 │
React Frontend
 │
API Calls
 │
Application Load Balancer
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
- Secure Checkout
- Razorpay Payment Integration
- Order Management
- User Authentication
- Cloud-native Deployment
- Dockerized Microservices

----
# 🛠️ Tech Stack

| Category | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | React.js | User Interface |
| **Backend** | Node.js + Express.js | REST APIs |
| **Database** | MySQL | Persistent Storage |
| **Containerization** | Docker | Package Microservices |
| **Container Registry** | Amazon ECR | Store Docker Images |
| **Container Orchestration** | Amazon ECS Fargate | Run Containers |
| **CI/CD** | Jenkins | Automated Build & Deployment |
| **Cloud Storage** | Amazon S3 | React Frontend Hosting |
| **Content Delivery** | Amazon CloudFront | CDN |
| **DNS** | Amazon Route 53 | Domain Management |
| **SSL** | AWS Certificate Manager | HTTPS Certificates |
| **Messaging** | Amazon SQS | Event-driven Communication |
| **Payments** | Razorpay | Payment Gateway |
| **Version Control** | Git & GitHub | Source Code Management |

---

# ☁️ AWS Infrastructure

The application is deployed using a secure AWS architecture that separates public-facing resources from backend services running inside a private network.

| AWS Service | Purpose |
|--------------|---------|
| **Amazon VPC** | Isolated network for the application |
| **Public Subnet** | Hosts the Application Load Balancer |
| **Private Subnet** | Hosts ECS Fargate Tasks & Amazon RDS |
| **Internet Gateway** | Allows public internet access |
| **NAT Gateway** | Outbound internet for private resources |
| **Application Load Balancer** | Routes API requests |
| **Amazon ECS Fargate** | Hosts backend microservices |
| **Amazon ECR** | Stores Docker container images |
| **Amazon RDS (MySQL)** | Application Database |
| **Amazon SQS** | Asynchronous communication between services |
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
Build Docker Images
     │
Push Images
     ▼
Amazon ECR
     │
Deploy Latest Images
     ▼
Amazon ECS Fargate
     │
Rolling Deployment
     ▼
Application Load Balancer
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

- Kubernetes (Amazon EKS)
- Terraform Infrastructure as Code
- CloudWatch Monitoring
- AWS Secrets Manager
- Auto Scaling
- Multi-AZ Deployment
- Blue/Green Deployment
- API Gateway
- AWS WAF
- Redis Caching
- Elasticsearch
- Amazon ElastiCache
- AWS CodePipeline

---

# 👩‍💻 Author

<div align="center">

## Rozana IM

Cloud Engineer • DevOps Engineer • AWS Enthusiast

GitHub: https://github.com/rozana09

LinkedIn: https://linkedin.com/in/<your-profile>

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
