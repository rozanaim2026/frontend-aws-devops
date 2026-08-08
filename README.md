<h2 align="center">☁️ LUCCI — Cloud Native E-Commerce Platform on AWS</h2>

<p align="center">
  <img src="./assets/LUCCI%20Architecture%20diagram.png" width="90%">
</p>

<br/>

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

---

# 📑 Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [AWS Infrastructure](#-aws-infrastructure)
- [Microservices](#-microservices)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Application Flow](#-application-flow)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Deployment](#-deployment)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

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

---

# 🏗️ Architecture

<p align="center">
<img src="./assets/LUCCI%20Architecture%20diagram.png" width="100%">
</p>

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

# 📦 Microservices

LUCCI follows a **Microservices Architecture**, where each business capability is deployed independently.

---

## 👤 User Service

Responsible for:

- User Registration
- User Login
- Authentication
- User Profile
- Account Management

---

## 📦 Product Service

Responsible for:

- Product Listing
- Categories
- Search Products
- Product Details
- Inventory Management

---

## 🛒 Order Service

Responsible for:

- Create Orders
- Order History
- Order Status
- Purchase Records

---

## 💳 Payment Service

Responsible for:

- Razorpay Integration
- Payment Verification
- Publish Payment Events
- Payment Status

---

# 🔄 CI/CD Pipeline

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

# 🔐 Security Architecture

LUCCI follows AWS security best practices.

### Network Security

- Amazon VPC
- Public & Private Subnets
- Security Groups
- Internet Gateway
- NAT Gateway

---

### Application Security

- HTTPS using AWS Certificate Manager
- Application Load Balancer
- IAM Roles & Policies
- Private Database
- Private ECS Tasks

---

### Database Security

- Amazon RDS deployed inside Private Subnet
- Accessible only from ECS Security Group
- No Public Internet Access

---

### Payment Security

- Razorpay Payment Gateway
- Payment Verification
- Amazon SQS Event Queue
- Order Confirmation after Successful Payment

---

# 🌐 Frontend Architecture

```
User
 │
 ▼
Amazon Route53
 │
 ▼
Amazon CloudFront
 │
 ▼
Amazon S3
 │
 ▼
React Application
 │
 ▼
API Requests
 │
 ▼
Application Load Balancer
 │
 ▼
Amazon ECS Fargate
```

---

# 🔄 Backend Request Flow

```
Client
   │
Application Load Balancer
   │
───────────────
User Service
Product Service
Order Service
Payment Service
───────────────
       │
Amazon RDS MySQL
       │
Amazon SQS
       │
Order Processing
```

---

# 📂 Project Structure

```text
LUCCI/
│
├── frontend/
│
├── user-service/
│
├── product-service/
│
├── order-service/
│
├── payment-service/
│
├── assets/
│   ├── LUCCI Architecture diagram.png
│   ├── HomePage.png
│   ├── Collections.png
│   ├── Womens.png
│   ├── Products.png
│   ├── CheckoutPage.png
│   ├── PaymentProcess.png
│   └── PaymentSuccessfull.png
│
├── Jenkinsfile
│
├── Dockerfile
│
└── README.md
```

---

# 📸 Application Screenshots

<div align="center">

### 🏠 Home Page & 🛍️ Collections

<p align="center">
  <img src="./assets/HomePage.png" alt="Home Page" width="48%">
  <img src="./assets/Collections.png" alt="Collections" width="48%">
</p>

---

### 👗 Women's Collection & 📦 Products

<p align="center">
  <img src="./assets/Womens.png" alt="Women's Collection" width="48%">
  <img src="./assets/Products.png" alt="Products" width="48%">
</p>

---

### 🛒 Checkout & 💳 Payment Process

<p align="center">
  <img src="./assets/CheckoutPage.png" alt="Checkout Page" width="48%">
  <img src="./assets/PaymentProcess.png" alt="Payment Process" width="48%">
</p>

---

### ✅ Payment Successful

<p align="center">
  <img src="./assets/PaymentSuccessfull.png" alt="Payment Successful" width="60%">
</p>

</div>
---

# 🚀 Deployment

## Clone Repository

```bash
git clone https://github.com/<your-github-username>/lucci.git

cd lucci
```

---

## Build Docker Images

```bash
docker build -t user-service ./user-service

docker build -t product-service ./product-service

docker build -t order-service ./order-service

docker build -t payment-service ./payment-service
```

---

## Push Images to Amazon ECR

```bash
docker tag user-service <your-ecr-uri>/user-service:latest
docker push <your-ecr-uri>/user-service:latest

docker tag product-service <your-ecr-uri>/product-service:latest
docker push <your-ecr-uri>/product-service:latest

docker tag order-service <your-ecr-uri>/order-service:latest
docker push <your-ecr-uri>/order-service:latest

docker tag payment-service <your-ecr-uri>/payment-service:latest
docker push <your-ecr-uri>/payment-service:latest
```

---

## Deploy using Jenkins

The Jenkins pipeline automatically performs:

- Checkout latest source code
- Build Docker images
- Push images to Amazon ECR
- Deploy latest containers to Amazon ECS Fargate
- Verify deployment

---

# 💻 Run Locally

### Install Dependencies

```bash
npm install
```

---

### Start Frontend

```bash
npm run dev
```

---

### Start Backend Services

```bash
npm start
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

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Cloud Native Application Development
- Microservices Architecture
- Docker Containerization
- Continuous Integration & Continuous Deployment
- Amazon ECS Fargate
- Amazon Elastic Container Registry (ECR)
- Amazon Relational Database Service (RDS)
- Amazon Simple Queue Service (SQS)
- Amazon CloudFront
- Amazon S3 Static Website Hosting
- Amazon Route53
- Application Load Balancer
- AWS Certificate Manager
- Amazon VPC Networking
- Public & Private Subnets
- Security Groups
- IAM
- Jenkins Automation
- Event-Driven Architecture

---

# 📋 Deployment Checklist

- [x] React Frontend Developed
- [x] Dockerized Microservices
- [x] Jenkins CI/CD Pipeline
- [x] Amazon ECR Integration
- [x] Amazon ECS Fargate Deployment
- [x] Application Load Balancer
- [x] Amazon RDS Database
- [x] Amazon SQS Integration
- [x] Amazon S3 Frontend Hosting
- [x] CloudFront Distribution
- [x] Route53 DNS
- [x] HTTPS using AWS Certificate Manager
- [x] Razorpay Payment Gateway

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
