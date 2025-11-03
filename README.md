# 🧠 Insurance Premium Predictor

This project uses a **Random Forest model** to predict an individual's **insurance premium category** based on features such as **age, weight, height, income, smoking habits, city, and occupation**.  
The entire application is **containerized using Docker** and can be deployed on any environment, including **AWS EC2**.

---

## ⚙️ Prerequisites

Before running the project, make sure you have the following installed:

- **Python 3.10**
- **Docker Engine**
- *(Optional)* Git for cloning the repository

---

## 🚀 Setup and Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/insurance-predictor.git
cd insurance-predictor
```

### 2. Create a Python environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
📘 *Installs all required Python packages for model training and serving.*

---

## 🐳 Docker Usage

### 1. Build the Docker image
```bash
docker build -t anxone/insurance-predictor .
```
🛠️ *Builds a Docker image from the Dockerfile and tags it as `anxone/insurance-predictor`.*

### 2. Run the Docker container
```bash
docker run -p 8501:8501 anxone/insurance-predictor
```
🌐 *Runs the container and maps port 8501 (used by Streamlit or FastAPI) from the container to your local machine.*

---

## ☁️ Pushing to Docker Hub

### Push the image
```bash
docker push anxone/insurance-predictor
```
📤 *Uploads your built Docker image to your Docker Hub repository (`anxone/insurance-predictor`).*

---

## 🧩 Installing Docker on Ubuntu (if not already installed)

### Update system and install Docker
```bash
sudo apt update && sudo apt upgrade
sudo apt install docker.io
```
🔧 *Updates system packages and installs Docker.*

### Start and enable Docker service
```bash
sudo systemctl start docker
sudo systemctl enable docker
```
⚙️ *Ensures Docker starts automatically after reboot.*

### Add outside server access (in this instance docker hub) to our EC3 instance
```bash
sudo usermod -aG docker $USER
```
---

## 🐋 Pulling and Running from Docker Hub

### Pull the latest image
```bash
docker pull anxone/insurance-predictor:latest
```
⬇️ *Downloads the latest version of the image from Docker Hub.*

### Run the container
```bash
docker run -p 8501:8501 anxone/insurance-predictor
```
🚀 *Runs the pre-built image locally.*

---

## 🌍 Access the Application

### Configure Inbound Rules (for EC2 deployment)

In your AWS EC2 instance’s **Security Group**, add an inbound rule:

| Type | Port | Source |
|------|------|---------|
| Custom TCP | 8501 | Anywhere (0.0.0.0/0) |

### This way anyone from outside computer/system can send request to our EC3 instance or to our endpoint.

### Visit the app in your browser
```
http://<your-ec2-public-ip>:8501/docs
```
💻 *Opens the API or web interface for the Insurance Predictor.*

---
