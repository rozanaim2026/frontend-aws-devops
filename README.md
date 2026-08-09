<div align="center">

# 🛍️ LUCCI Frontend (Free-Tier Deployment)

----
### Frontend Application for the LUCCI Cloud Native E-Commerce Platform
<br/>

<div align="center">

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)

</div>

<br/>

> Built using **HTML5 + CSS3 + JavaScript**
>
> Deployed as a static site on **Vercel** (free tier), pushed directly from the CLI
>
> Communicates with backend microservices — each hosted independently on **Render**

<br/>

### 🔗 [Live Demo](https://frontend-aws-devops-1.vercel.app)

> ⚠️ Backend services run on Render's free tier and may take 20-30 seconds to respond on first load after a period of inactivity (cold start).

</div>

----

# 📑 Table of Contents

- [Overview](#overview)
- [Why a Free-Tier Branch](#why-a-free-tier-branch)
- [Frontend Responsibilities](#frontend-responsibilities)
- [Project Repositories](#project-repositories)
- [Architecture](#architecture)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Deployment Flow](#deployment-flow)
- [Frontend Repository Structure](#frontend-repository-structure)
- [Getting Started](#getting-started)
- [Environment Configuration](#environment-configuration)
- [Future Improvements](#future-improvements)
- [Author](#author)

----

<a id="overview"></a>
# 🔍 Overview

This branch (`free-tier-deploy`) contains the customer-facing frontend for the LUCCI Cloud Native E-Commerce Platform, re-architected to run entirely on **free-tier infrastructure** instead of AWS.

The frontend is static HTML5, CSS3, and vanilla JavaScript, deployed to **Vercel** and served over Vercel's global CDN. Product images and static assets are committed directly into the repository rather than served from a cloud bucket, keeping the stack dependency-free and cost-free.

The complete LUCCI platform consists of:

- Frontend (this repo)
- User Service
- Product Service
- Order Service
- Payment Service

----

<a id="why-a-free-tier-branch"></a>
# 💡 Why a Free-Tier Branch

The `main` branch of this repository documents the original AWS-based architecture (S3, CloudFront, Route 53). This `free-tier-deploy` branch is a parallel implementation of the same application, rebuilt to run at **zero infrastructure cost** — useful as a permanently live portfolio demo without ongoing AWS billing.

Both branches are preserved so the AWS architecture and reasoning remain documented, while this branch stays live and accessible.

----

<a id="frontend-responsibilities"></a>
# 🌐 Frontend Responsibilities

The frontend application is responsible for:

- Displaying products and collections
- Managing the shopping cart and wishlist
- Handling the checkout and Razorpay payment experience
- Managing user sessions (JWT-based)
- Displaying order history and order details
- Providing an admin dashboard for managing users, orders, and products
- Integrating with four independently deployed backend REST APIs
- Providing a responsive shopping experience across devices

----

<a id="project-repositories"></a>
# 📦 Project Repositories

| Repository | Description |
|------------|-------------|
| **[Frontend](https://github.com/rozanaim2026/frontend-aws-devops)** *(Current Repository)* | Customer-facing web application |
| **[User Service](https://github.com/rozanaim2026/user-service)** | Authentication & User Management |
| **[Product Service](https://github.com/rozanaim2026/product-service)** | Product Catalog |
| **[Order Service](https://github.com/rozanaim2026/order-service)** | Order Processing |
| **[Payment Service](https://github.com/rozanaim2026/payment-service)** | Razorpay Integration |

----

<a id="architecture"></a>
# Architecture
### Architecture Flow

```
Users
   │
Vercel Edge Network
   │
Static Frontend (HTML/CSS/JS)
   │
REST API Requests
   ▼
┌─────────────────────────────────────────────┐
│  User Service     (Render)                   │
│  Product Service  (Render)                   │
│  Order Service    (Render)                   │
│  Payment Service  (Render)                   │
└─────────────────────────────────────────────┘
   │
Aiven PostgreSQL (shared database instance)
```

### Request Flow

1. Users access the application via its Vercel-assigned domain.
2. Static frontend assets are served from Vercel's global CDN.
3. The frontend sends REST API requests **directly to each backend microservice's own Render URL** — there is no shared load balancer or API gateway in this deployment; each service is called at its own independent hostname.
4. Backend microservices process the requests against a shared Aiven PostgreSQL instance and return JSON responses to the frontend.

> **Note:** Unlike the AWS version's single ALB with path-based routing, the free-tier deployment calls each microservice's Render URL directly from the frontend (`USER_API`, `PRODUCT_API`, `ORDER_API`, `PAYMENT_API` constants in `config.js`).

----

<a id="features"></a>
## ✨ Features

- Responsive HTML5, CSS3 & JavaScript Frontend
- Product Browsing & Category Collections
- Live Product Search
- Product Details
- Shopping Cart & Wishlist
- Checkout Workflow with Razorpay (test mode)
- Order Tracking & Order History
- User Profile & Persistent Login
- Admin Dashboard (Users / Orders / Products / Service Health)
- REST API Integration across 4 independent microservices
- Cloud-native, zero-cost deployment

----

<a id="tech-stack"></a>
# Tech Stack
| Category | Technology | Purpose |
|-----------|------------|---------|
| Frontend | HTML5 | Structure |
| Styling | CSS3 | User Interface |
| Scripting | JavaScript (ES6) | Client-side Functionality |
| Payments | Razorpay (test mode) | Checkout |
| Hosting | Vercel | Static Site Hosting + CDN |
| Deployment | Vercel CLI | Direct deploy from local build |
| Version Control | Git & GitHub | Source Code Management |

----

<a id="deployment-flow"></a>
# 🚀 Deployment Flow

```
Developer
     │
Local Build (public/ folder)
     ▼
Vercel CLI (`vercel --prod`)
     ▼
Vercel Edge Network
     ▼
Live Site
```

Unlike the AWS branch's Jenkins-driven pipeline, this branch deploys directly from the developer's machine using the Vercel CLI. This was a deliberate simplification — Vercel's free tier does not require a CI/CD pipeline for a static site of this size, and avoids extra GitHub App/OAuth configuration.

----

<a id="frontend-repository-structure"></a>
# 📁 Frontend Repository Structure

| Folder / File | Description |
|---------------|-------------|
| `public/` | Deployed root — everything Vercel serves lives here |
| `public/assets/` | Product and category images (committed locally, no external CDN) |
| `public/src/` | JavaScript logic for frontend features |
| `public/components/` | Reusable HTML components (Navbar, etc.) |
| `public/config.js` | Defines `USER_API`, `PRODUCT_API`, `ORDER_API`, `PAYMENT_API` — the four backend service URLs |
| `public/index.html` | Landing page |
| `public/products.html` | Product listing / category selector |
| `public/product-details.html` | Product details page |
| `public/collections.html` | Category product listing |
| `public/search.html` | Live product search |
| `public/cart.html` | Shopping cart |
| `public/checkout.html` | Checkout workflow with Razorpay |
| `public/orders.html` | User order history |
| `public/order-details.html` | Individual order details |
| `public/order-success.html` | Order confirmation |
| `public/wishlist.html` | Wishlist management |
| `public/profile.html` | User login / profile |
| `public/admin.html` | Admin dashboard |
| `public/contact.html` | Contact page |
| `public/style.css` | Global styling |

----

<a id="getting-started"></a>
# 🚀 Getting Started

## Clone the Repository

```bash
git clone -b free-tier-deploy https://github.com/rozanaim2026/frontend-aws-devops.git
cd frontend-aws-devops
```

## Run Locally

```bash
npx serve public -l 3000
```

The application will be available at:

```text
http://localhost:3000
```

## Deploy to Vercel

```bash
npm install -g vercel
cd public
vercel login
vercel --prod
```

----

<a id="environment-configuration"></a>
# Environment Configuration
Since this is a static site, there is no `.env` file — service URLs are defined directly in `public/config.js`:

```js
const USER_API = "https://lucci-user-service.onrender.com";
const PRODUCT_API = "https://lucci-product-service.onrender.com";
const ORDER_API = "https://order-service-wuwi.onrender.com";
const PAYMENT_API = "https://payment-service-x7m0.onrender.com";
```

----

<a id="future-improvements"></a>
# 📈 Future Improvements

- Progressive Web App (PWA)
- Dark Mode
- Accessibility Improvements (WCAG)
- Image optimization and lazy loading
- Frontend unit testing
- Reconnect Git-based auto-deploy (currently manual via CLI)

----

<a id="author"></a>
# Author
<div align="center">

## Rozana IM

Cloud Engineer • DevOps Engineer • AWS Enthusiast

GitHub: https://github.com/rozanaim2026

LinkedIn: https://www.linkedin.com/in/rozana-im-a63541302/

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

---

## ☁️ Built with HTML5 • CSS3 • JavaScript • Vercel

### ❤️ Part of the LUCCI Cloud Native E-Commerce Platform (Free-Tier Edition)
</div>
