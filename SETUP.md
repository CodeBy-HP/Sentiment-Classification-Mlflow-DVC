# 🚀 Setup & Deployment Guide

Complete instructions for running the Sentiment Classification MLOps pipeline locally or deploying to AWS.

---

## 📋 Prerequisites

- Python 3.10+
- Git
- Docker (for containerization)
- AWS Account (for cloud deployment)
- DagShub Account (for MLOps tracking)

---

## 🏠 Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/CodeBy-HP/Sentiment-Classification.git
cd Sentiment-Classification
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data

```bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet')"
```

### 5. Setup Environment Variables

Create a `.env` file in the root directory:

```env
# MLflow & DagShub
MLFLOW_TRACKING_URI=https://dagshub.com/your-username/Sentiment-Classification.mlflow
MLFLOW_TRACKING_USERNAME=your-dagshub-username
MLFLOW_TRACKING_PASSWORD=your-dagshub-token

# AWS (optional for S3)
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_DEFAULT_REGION=us-east-1
```

### 6. Initialize DVC

```bash
dvc pull  # Pull data from remote storage
```

---

## 🔄 Running the ML Pipeline

### Execute Complete Pipeline

```bash
dvc repro
```

This runs all stages:
1. Data ingestion
2. Preprocessing
3. Feature engineering
4. Model training
5. Evaluation
6. Model registration

### Run Individual Stages

```bash
dvc repro data_ingestion
dvc repro feature_engineering
# ... etc
```

### View Pipeline DAG

```bash
dvc dag
```

---

## 📊 MLflow Tracking

### Start MLflow UI Locally

```bash
mlflow ui
```

Visit: `http://localhost:5000`

### View on DagShub

Visit your DagShub repository → MLflow tab to see:
- All experiments
- Model metrics
- Registered models
- Model versions

---

## 🧪 Running Tests

### Run All Tests

```bash
pytest tests/
```

### Run Specific Tests

```bash
# Test model
pytest tests/test_model.py

# Test FastAPI app
pytest tests/test_fastapi_app.py
```

### With Coverage

```bash
pytest tests/ --cov=sentiment_classification
```

---

## 🌐 Running FastAPI App Locally

### Start the Server

```bash
cd fastapi_app
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Access the Application

- Web UI: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`

### Test Prediction

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie was absolutely amazing!"}'
```

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t sentiment-classification:latest .
```

### Run Container

```bash
docker run -d \
  --name sentiment-app \
  -p 8000:8000 \
  -v $(pwd)/models:/app/models \
  sentiment-classification:latest
```

### Test Running Container

```bash
curl http://localhost:8000/health
```

### View Logs

```bash
docker logs -f sentiment-app
```

### Stop Container

```bash
docker stop sentiment-app
docker rm sentiment-app
```

---

## ☁️ AWS Deployment

### Prerequisites

- AWS CLI configured (`aws configure`)
- ECR repository created
- EC2 instance running (Ubuntu recommended)

### 1. Push to AWS ECR

```bash
# Authenticate Docker to ECR
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com

# Tag image
docker tag sentiment-classification:latest \
  <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com/sentiment-classification:latest

# Push to ECR
docker push <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com/sentiment-classification:latest
```

### 2. Deploy to EC2

SSH into your EC2 instance:

```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

Install Docker on EC2:

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo usermod -aG docker ubuntu
```

Pull and run container:

```bash
# Login to ECR
aws ecr get-login-password --region us-east-1 | \
  sudo docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com

# Pull image
sudo docker pull <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com/sentiment-classification:latest

# Run container
sudo docker run -d \
  --name sentiment-app \
  -p 80:8000 \
  --restart unless-stopped \
  <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com/sentiment-classification:latest
```

### 3. Configure Security Group

- Allow inbound traffic on port 80 (HTTP)
- Allow inbound traffic on port 8000 (if testing directly)

### 4. Access Application

Visit: `http://your-ec2-public-ip`

---

## 🔄 CI/CD Setup (GitHub Actions)

### 1. Add GitHub Secrets

Go to your repo → Settings → Secrets and add:

```
CAPSTONE_TEST
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
AWS_ACCOUNT_ID
ECR_REPOSITORY
```

### 2. Setup Self-Hosted Runner (EC2)

On your EC2 instance:

```bash
# Download runner
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.311.0.tar.gz -L \
  https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz
tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz

# Configure
./config.sh --url https://github.com/your-username/Sentiment-Classification --token YOUR_TOKEN

# Run as service
sudo ./svc.sh install
sudo ./svc.sh start
```

### 3. Trigger Deployment

Push code to `main` branch:

```bash
git add .
git commit -m "Deploy new model"
git push origin main
```

GitHub Actions will:
1. Run DVC pipeline
2. Test model quality
3. Promote if better
4. Test API
5. Build Docker image
6. Push to ECR
7. Deploy to EC2

---

## 🔍 Monitoring & Logs

### View Container Logs

```bash
docker logs -f sentiment-app
```

### Check Health

```bash
curl http://localhost:8000/health
```

### MLflow Metrics

Check DagShub for real-time metrics and experiment tracking.

---


**Happy Experimenting! 🚀**
