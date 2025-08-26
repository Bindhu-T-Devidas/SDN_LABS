# Streamlit DevOps Lab (Beginner Friendly)

This is the tiniest possible lab to learn **Git/GitHub + CI (GitHub Actions)**, **Docker + Docker Hub**, and **Kubernetes** using a single Streamlit app.

## 0) Run locally (no Docker)
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
App: http://localhost:8501

---

## 1) Git + GitHub + CI
```bash
git init
git add .
git commit -m "feat: minimal streamlit app"
git branch -M main
git remote add origin https://github.com/<YOUR_USER>/streamlit-devops-lab.git
git push -u origin main
```
CI runs automatically (see **Actions** tab).

---

## 2) Docker + Docker Hub
Build and run:
```bash
docker build -t streamlit-devops-lab:local .
docker run -p 8501:8501 streamlit-devops-lab:local
# open http://localhost:8501
```

Push to Docker Hub (replace `YOUR_DH_USERNAME`):
```bash
docker tag streamlit-devops-lab:local YOUR_DH_USERNAME/streamlit-devops-lab:v1
docker login
docker push YOUR_DH_USERNAME/streamlit-devops-lab:v1
```

---

## 3) Kubernetes (Minikube)
Install Minikube + kubectl (macOS example):
```bash
brew install minikube kubectl
minikube start
```

Edit `k8s/deployment.yaml` and set your Docker Hub image:
```yaml
image: YOUR_DH_USERNAME/streamlit-devops-lab:v1
```

Apply and open:
```bash
kubectl apply -f k8s/
minikube service streamlit-svc --url
# or auto-open:
minikube service streamlit-svc
```

Clean up:
```bash
kubectl delete -f k8s/
minikube stop
```

---

## Notes
- `APP_ENV` environment variable shows where the app is running: `local`, `container`, `k8s`.
- Keep things simple; this repo is for learning, not production.