# IoT API Service (FastAPI)

A scalable IoT API service built with FastAPI, Docker, and PostgreSQL, deployed to AWS ECS using GitHub Actions for CI/CD. Developed as part of a DevOps case study.

---

## 🚀 Features

- FastAPI backend for IoT sensor data
- REST endpoints to POST and GET readings
- PostgreSQL database for persistent storage
- Dockerized for consistent deployment
- GitHub Actions for CI/CD to Amazon ECS
- Scalable architecture using ECS and ECR

---

## 📦 Tech Stack

- **FastAPI** – lightweight web framework
- **PostgreSQL** – database for sensor readings
- **Docker** – containerized microservices
- **GitHub Actions** – CI/CD pipeline
- **AWS ECS** – container orchestration (Fargate)
- **AWS ECR** – container registry

---

## 🔧 Project Structure

```
.
├── app/
│   └── main.py              # FastAPI app entry point
├── Dockerfile               # App container build file
├── docker-compose.yml       # Local development setup
├── .aws/
│   └── task-definition.json # ECS task definition file
├── .github/workflows/
│   └── ci-cd.yml           # CI/CD pipeline config
└── README.md
```

---

## 🧪 Run Locally

Start the API and database locally with Docker:

```bash
docker-compose up --build
```

Or run the app directly for quick testing:

```bash
uvicorn app.main:app --reload
```

Access the API at `http://localhost:8000`

---

## 📥 API Endpoints

| Method | Endpoint         | Description           |
|--------|------------------|-----------------------|
| GET    | `/`              | Health check          |
| POST   | `/sensor`        | Submit sensor reading |
| GET    | `/sensor`        | List all readings     |

---

## 🐳 Docker Compose Services

- `iot-api` – FastAPI app container
- `iot-db` – PostgreSQL database container

Health checks ensure the app waits until the DB is ready.

---

## 🛠 CI/CD via GitHub Actions

Workflow `.github/workflows/ci-cd.yml` does the following on push to `main`:

1. Logs into AWS ECR
2. Builds and pushes Docker image
3. Renders ECS task definition
4. Deploys updated task to ECS cluster

You must configure these in `ci-cd.yml`:

```yaml
env:
  AWS_REGION: us-east-1
  ECR_REPOSITORY: iot-api
  ECS_SERVICE: iot-api-service
  ECS_CLUSTER: iot-api-cluster
  ECS_TASK_DEFINITION: .aws/task-definition.json
  CONTAINER_NAME: iot-api-container
```

### 🔐 Required GitHub Secrets

| Secret Name            | Description              |
|------------------------|--------------------------|
| `AWS_ACCESS_KEY_ID`    | IAM user access key      |
| `AWS_SECRET_ACCESS_KEY`| IAM secret key           |
| 'DOCKER_USERNAME'      | Docker Hub username      |
| 'DOCKER_PASSWORD'      | Docker  Hub Password     |

---

## 📄 ECS Task Definition

Example task definition (`.aws/task-definition.json`):

```json
{
  "family": "iot-api-task",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "containerDefinitions": [
    {
      "name": "iot-api-container",
      "image": "REPLACE_ME",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 8000
        }
      ]
    }
  ]
}
```

---

## 🏁 Production Workflow

1. Push code to `main`
2. GitHub builds Docker image and uploads to ECR
3. ECS Task Definition updated with new image
4. ECS Service updated with zero downtime

---

## ✅ Next Steps

- Add unit tests and coverage reporting
- Configure ALB for HTTPS + custom domain
- Integrate AWS Secrets Manager for DB credentials
- Add monitoring via CloudWatch and X-Ray

---

## 👤 Author

Deborah Njeri Munene  
DevOps | Cloud | Machine Learning  
