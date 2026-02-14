# Cloud Web Application (FastAPI + Docker + CI/CD + AWS)

## Project Overview
This project is a professional-level cloud web application built using modern DevOps practices.  
It demonstrates containerization, CI/CD automation, and cloud deployment on AWS.

The application is a simple FastAPI service with production-style endpoints and a complete deployment pipeline.

---

## Architecture
Developer → GitHub → GitHub Actions → Docker Hub → AWS EC2 → Docker Container → Browser

---

## Features
- FastAPI backend application
- Health check endpoint
- API message endpoint
- Dockerized application
- Automated CI/CD pipeline using GitHub Actions
- Deployed on AWS EC2

---

## Tech Stack

| Layer | Tool |
|------|------|
| Backend | FastAPI (Python) |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud | AWS EC2 |
| Image Registry | Docker Hub |

---

## Application Endpoints

| Endpoint | Description |
|---------|-------------|
| `/` | Welcome message |
| `/health` | Health check endpoint |
| `/api/message` | Sample API response |

---

## Project Structure

cloud-web-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/
└── workflows/
└── docker.yml


---

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/cloud-web-app.git
cd cloud-web-app
2. Build Docker image
docker build -t cloud-app .
3. Run container
docker run -d -p 5000:5000 cloud-app
4. Open in browser
http://localhost:5000
CI/CD Pipeline
The project uses GitHub Actions to:

Build the Docker image

Push the image to Docker Hub automatically

Enable automated deployment workflows

Pipeline triggers on every push to the main branch.

Deployment on AWS
The application is deployed on an AWS EC2 instance:

Launch EC2 instance

Install Docker

Pull image from Docker Hub

Run container

Access via public IP


