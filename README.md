# 🌸 Flower Payment Platform

A production-style Flask Payment API demonstrating an end-to-end DevOps lifecycle using Git, GitHub, GitHub Actions, Docker, Kubernetes, Helm, Terraform, security scanning, monitoring, and troubleshooting.

## 🚀 Project Overview

This project demonstrates how a Python Flask API can be developed, tested, containerized, deployed to Kubernetes, packaged with Helm, automated using Infrastructure as Code, and monitored using Kubernetes tools.

The project is designed as a practical DevOps/SRE portfolio project covering the workflow from **code development to production-style deployment and operations**.

## 🏗️ DevOps Architecture

```text
Developer
    |
    v
Git
    |
    v
GitHub
    |
    v
GitHub Actions
    |
    +----> Automated Tests
    |
    +----> Docker Build
    |
    v
Docker Image
    |
    v
Kubernetes / Minikube
    |
    +----> Deployment
    |         |
    |         +----> 3 Replicas
    |
    +----> Service
    |
    +----> Rolling Update
    |
    +----> Rollback
    |
    v
Helm
    |
    v
Monitoring + Logs
    |
    v
Production-style Troubleshooting

Terraform
    |
    v
Infrastructure as Code

Trivy
    |
    v
Container Security Scanning
```

## 🛠️ Technologies

| Category               | Tools                     |
| ---------------------- | ------------------------- |
| Application            | Python, Flask             |
| Testing                | Pytest                    |
| Version Control        | Git, GitHub               |
| CI                     | GitHub Actions            |
| Containerization       | Docker                    |
| Orchestration          | Kubernetes                |
| Local Kubernetes       | Minikube                  |
| Package Management     | Helm                      |
| Infrastructure as Code | Terraform                 |
| Security               | Trivy                     |
| Monitoring             | Kubernetes Metrics Server |
| Logging                | Kubernetes Logs           |
| Environment            | Linux / WSL               |

## 📁 Project Structure

```text
flower-payment-platform/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── routes.py
│
├── tests/
│   └── test_api.py
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── helm/
│   └── payment-api/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│
├── terraform/
│   └── main.tf
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔌 API

### Health Check

```http
GET /health
```

Example response:

```json
{
  "service": "payment-api",
  "status": "healthy"
}
```

## 🧪 Testing

The project contains automated Pytest tests for API functionality and validation.

Run:

```bash
python -m pytest -v
```

Current test result:

```text
6 passed
```

Tests cover:

* Health endpoint
* Payment creation
* Invalid payment amount
* Missing customer
* Payment retrieval
* Invalid amount type

## 🐳 Docker

Build the Docker image:

```bash
docker build -t payment-api .
```

Run the container:

```bash
docker run -p 5000:5000 payment-api
```

## ☸️ Kubernetes

The application is deployed to Kubernetes using Deployment and Service manifests.

Apply the Kubernetes resources:

```bash
kubectl apply -f k8s/
```

Check deployments:

```bash
kubectl get deployments
```

Check pods:

```bash
kubectl get pods
```

Check services:

```bash
kubectl get svc
```

### Kubernetes capabilities demonstrated

* Multiple replicas
* Scaling
* NodePort service
* Rolling updates
* Rollback
* Pod health verification
* Logs and troubleshooting
* Resource monitoring

## ⎈ Helm

The application is also packaged using Helm.

Install:

```bash
helm install payment-api-helm ./helm/payment-api
```

Check releases:

```bash
helm list
```

Check Helm-managed resources:

```bash
kubectl get pods
kubectl get svc
```

## 🏗️ Terraform

Terraform is used to demonstrate Infrastructure as Code.

Typical workflow:

```bash
terraform init
terraform plan
terraform apply
```

Terraform configuration is located in:

```text
terraform/main.tf
```

Terraform state files and provider files are excluded from Git using `.gitignore`.

## 🔐 Security Scanning

Trivy is used to scan Docker images for known vulnerabilities.

Example:

```bash
trivy image payment-api:latest
```

This provides an additional security validation step before deployment.

## 📊 Monitoring

Kubernetes resource monitoring can be performed using:

```bash
kubectl top pods
kubectl top nodes
```

This helps monitor:

* CPU usage
* Memory usage
* Pod resource consumption
* Node resource consumption

## 📝 Logging & Troubleshooting

Application logs can be inspected using:

```bash
kubectl logs <pod-name>
```

Detailed pod information:

```bash
kubectl describe pod <pod-name>
```

These commands help troubleshoot:

* Application failures
* Container crashes
* Pod scheduling problems
* Deployment issues
* Configuration problems

## 🔄 CI Pipeline

GitHub Actions is configured to automatically validate code changes.

Pipeline:

```text
Git Push
    |
    v
GitHub Actions
    |
    v
Setup Python
    |
    v
Install Dependencies
    |
    v
Run Pytest
    |
    v
Build Docker Image
```

This provides automated validation before changes are considered ready for deployment.

## 🔄 SDLC / DevOps Lifecycle

```text
1. Planning
      ↓
2. Requirements
      ↓
3. Design
      ↓
4. Development
      ↓
5. Testing
      ↓
6. Git / GitHub
      ↓
7. CI with GitHub Actions
      ↓
8. Docker
      ↓
9. Kubernetes
      ↓
10. Helm
      ↓
11. Terraform
      ↓
12. Security Scanning
      ↓
13. Monitoring
      ↓
14. Logging & Troubleshooting
      ↓
15. Continuous Improvement
```

## 🎯 Production-Style Scenarios

The project demonstrates practical DevOps/SRE scenarios including:

* API health monitoring
* Automated testing
* Container image creation
* Kubernetes deployment
* Running multiple replicas
* Application scaling
* Rolling updates
* Deployment rollback
* Kubernetes log analysis
* Resource monitoring
* Infrastructure as Code
* Container vulnerability scanning
* CI pipeline validation

## ☁️ AWS Extension

The local Kubernetes implementation can be extended to AWS using Amazon ECR and Amazon EKS.

Target architecture:

```text
Developer
    |
    v
GitHub
    |
    v
GitHub Actions
    |
    +----> Pytest
    |
    +----> Docker Build
    |
    +----> Trivy Scan
    |
    v
Amazon ECR
    |
    v
Amazon EKS
    |
    +----> Kubernetes Pods
    |
    +----> Kubernetes Service
    |
    v
AWS Load Balancer
    |
    v
Payment API
    |
    v
Amazon CloudWatch
```

Terraform can be used to provision and manage the AWS infrastructure.

## 👩‍💻 Author

**Bhavya K P**

Cloud / DevOps Engineer

Technologies: AWS, Kubernetes, Docker, Terraform, GitHub Actions, Python, Linux, Monitoring and Production Support.

