<div align="center">

# 🎭 Sentiment Classification - MLOps Pipeline

*Production-grade sentiment analysis with automated experimentation, testing, and deployment*

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![MLflow](https://img.shields.io/badge/MLflow-2.15.0-0194E2.svg)](https://mlflow.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![DVC](https://img.shields.io/badge/DVC-Enabled-945DD6.svg)](https://dvc.org/)

</div>

---

## 🎯 Overview

End-to-end MLOps system for sentiment analysis featuring **automated experimentation**, **intelligent model promotion**, and **cloud deployment**. The pipeline systematically compares 10 model combinations and deploys only when quality improves.

---

## 🌈 User Interface

<img width="1393" height="701" alt="Screenshot 2025-12-17 155611" src="https://github.com/user-attachments/assets/bffd17aa-cc57-4fc1-89e3-d0837d923304" />

---

## 🌈 Video Demo

<!-- Add your demo video here -->

---

## 🌈 Architecture and Workflow Diagrams

<img width="754" height="792" alt="Screenshot 2025-12-17 155305" src="https://github.com/user-attachments/assets/f08d4f8e-984b-4fbc-b10b-2b44176ec1f1" />

<img width="773" height="661" alt="Screenshot 2025-12-17 155321" src="https://github.com/user-attachments/assets/86976a84-dd14-480e-8b8b-601b9febba99" />

<img width="518" height="836" alt="Screenshot 2025-12-17 155355" src="https://github.com/user-attachments/assets/d0b4a76a-bdba-4cae-8f70-8da2b4174bee" />

---

## ✨ Key Features

### 🔬 **SYSTEMATIC EXPERIMENTATION**
- Tested multiple models with BoW and TF-IDF
- Tracked all experiments using MLflow

### 🔄 **AUTOMATED ML PIPELINE**
- End-to-end DVC pipeline for data → model
- Fully reproducible with versioned parameters

### 🎯 **SMART MODEL PROMOTION**
- Automatically promotes only high-quality models
- Uses MLflow registry for staging and production

### 🚀 **COMPLETE CI/CD PIPELINE**
- Automated builds and deployments via GitHub Actions
- Dockerized deployment on AWS EC2

### 🧪 **COMPREHENSIVE TESTING**
- Validates model performance and API endpoints
- Prevents faulty models from being deployed

### 🌐 **PRODUCTION-READY APPLICATION**
- FastAPI app for real-time sentiment prediction
- Clean UI with health and confidence checks

---

## 🛠️ Tech Stack

- **Machine Learning:** Pandas & NumPy, NLTK 
- **Mlops Tools:** MLflow, DVC, DagShub
- **Deployement & CICD:** Docker, GitHub Actions, AWS (EC2, ECR) , FastAPI

---

## 📁 Project Structure

```
Sentiment-Classification/
├── sentiment_classification/
│   ├── data/              # Data ingestion & preprocessing
│   ├── features/          # Feature engineering (BoW/TF-IDF)
│   ├── modeling/          # Training, evaluation, registry
│   └── connections/       # AWS S3 integration
├── fastapi_app/
│   ├── app.py            # FastAPI application
│   └── templates/        # Web interface
├── notebooks/            # Experimentation notebooks
├── scripts/
│   └── promote_model.py  # Smart model promotion
├── tests/                # Unit tests
├── data/                 # Dataset (tracked by DVC)
├── models/               # Saved models
├── .github/workflows/    # CI/CD pipeline
├── dvc.yaml              # DVC pipeline definition
└── Dockerfile            # Container configuration
```

---


## 🚀 Setup & Deployment

**Want to run this project?**

👉 **[Complete Setup Instructions](SETUP.md)**

Includes local setup, DVC pipeline execution, MLflow tracking, Docker deployment, and AWS deployment guide.


---


## 🎓 What I Learned

- Building reproducible ML pipelines with DVC
- Experiment tracking and model versioning with MLflow
- Conditional deployment strategies
- CI/CD for ML systems
- Docker containerization best practices
- AWS cloud deployment (ECR + EC2)
- Writing production-ready ML code
- Comprehensive testing for ML systems

---

## 🔮 Future Enhancements

- **Kubernetes**: Migrate to K8s for auto-scaling
- **Redis Caching**: Cache predictions for faster responses
- **Authentication**: Add user management with OAuth2/JWT
- **Monitoring**: Implement Prometheus + Grafana dashboards
- **A/B Testing**: Compare model versions in production
- **Explainability**: Add SHAP/LIME for prediction explanations

---

## 👤 Author

**Harsh Patel**  
📧 code.by.hp@gmail.com  
🔗 [GitHub](https://github.com/CodeBy-HP) • [LinkedIn](https://www.linkedin.com/in/harsh-patel-389593292/)

---

<div align="center">

**⭐ Star this repo if you find it useful**

</div>
