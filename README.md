
# CloudFlask Manager

**CloudFlask Manager** is a comprehensive DevOps project designed to manage and deploy a microservices application using modern tools and practices. This project involves building a Flask application, containerizing it with Docker, orchestrating it with Kubernetes, setting up CI/CD pipelines, and deploying it on AWS.

## Project Overview

### Features

- **Flask Application**: A simple Flask web application as the core service.
- **Docker**: Containerized the Flask application using Docker.
- **Kubernetes**: Orchestrated the containerized application with Kubernetes on AWS EKS.
- **CI/CD Pipelines**: Configured continuous integration and deployment pipelines.
- **AWS Deployment**: Deployed the application on AWS with scalable infrastructure.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- **AWS CLI**: Installed and configured with appropriate access.
- **Docker**: Installed for containerizing the application.
- **kubectl**: Installed for managing Kubernetes clusters.
- **eksctl**: Installed for creating and managing EKS clusters.
- **AWS Account**: With permissions to create and manage resources.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/TheAnalystAbdalrahman/cloudflask_manager.git
   cd cloudflask_manager
   ```

2. **Set Up Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Docker

1. **Build Docker Image**

   ```bash
   docker build -t cloudflask-manager .
   ```

2. **Run Docker Container**

   ```bash
   docker run -p 5000:5000 cloudflask-manager
   ```

### Kubernetes

1. **Create EKS Cluster**

   ```bash
   eksctl create cluster --name cloudflask-manager --region us-east-1 --nodes 3 --node-type t3.medium
   ```

2. **Deploy Application**

   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

3. **Verify Deployment**

   ```bash
   kubectl get deployments
   kubectl get services
   ```

## CI/CD Pipeline

Configure your CI/CD pipeline with your preferred tool (Jenkins, GitLab CI, GitHub Actions) to automate builds and deployments.

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [AWS EKS Documentation](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)

## Contact

- **GitHub**: [TheAnalystAbdalrahman](https://github.com/TheAnalystAbdalrahman)
- **Docker Hub**: [theanalystabdalrahman](https://hub.docker.com/u/theanalystabdalrahman)

Feel free to reach out with any questions or feedback!
```
