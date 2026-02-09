# Docker Deployment Guide for Health Assistant

This document explains how to build, run, and manage the Docker container for the Multiple Disease Prediction System.

## 🚀 Getting Started

### 1. Build the Docker Image
To create the Docker image using the provided `Dockerfile`, run the following command in the project root:

```bash
docker build -t disease-prediction-app:v1 .
```

- `-t disease-prediction-app:v1`: Names the image "disease-prediction-app" with a "v1" tag.
- `.`: Specifies the current directory as the build context.

### 2. Run the Container
Once the image is built, you can start the application in a detached container:

```bash
docker run -d -p 8502:8501 --name health-app-container disease-prediction-app:v1
```

- `-d`: Runs the container in the background (detached mode).
- `-p 8502:8501`: Maps port **8502** on your laptop to port **8501** inside the container.
- `--name health-app-container`: Gives a friendly name to the running container.

**Access the app at:** [http://localhost:8502](http://localhost:8502)

---

## 🛠️ How it Works

### The Dockerfile
The `Dockerfile` defines the environment:
1.  **Base Image**: Uses `python:3.12-slim` for a small footprint.
2.  **System Dependencies**: Installs `build-essential` and `curl` for package compatibility.
3.  **App Setup**: Sets `/app` as the working directory and copies `requirements.txt`.
4.  **Dependencies**: Runs `pip install` to set up the ML environment.
5.  **Entry Point**: Automatically launches Streamlit on container startup.

### The .dockerignore
The `.dockerignore` file prevents bulky or sensitive files from being copied into the image, such as:
- `venv/` (Local virtual environments)
- `.git/` (Version history)
- `dataset/` (Raw data not needed for inference)
- `__pycache__/` (Python cache files)

---

## 📋 Common Management Commands

| Action | Command |
| :--- | :--- |
| **View Running Containers** | `docker ps` |
| **Stop the Application** | `docker stop health-app-container` |
| **Start the Application** | `docker start health-app-container` |
| **View Logs** | `docker logs -f health-app-container` |
| **Remove Container** | `docker rm -f health-app-container` |
| **Remove Image** | `docker rmi disease-prediction-app:v1` |

---

## ✅ Prerequisites
- Ensure **Docker Desktop** is installed and running on your laptop.
- The `saved_models/` folder must be present in the project directory before building, as the code relies on these pre-trained models.
