# Local Kubernetes Testing Commands

Two options below: **Kind** (default) or **Minikube**. Run from repo root. Replace `<...>` placeholders (e.g., secrets).

## One-time prep
```bash
# Ensure tools are installed
docker version
kubectl version --client
kind version            # if using Kind
minikube version        # if using Minikube

# Create secrets file from the template
cp k8s/secrets-template.yaml k8s/secrets.yaml
$EDITOR k8s/secrets.yaml
```

## Option A: Kind
```bash
# 1) Create cluster + namespace
kind create cluster --name inventro-local
kubectl create namespace inventro

# 2) Build app image and load into cluster
docker build -t inventro:local .
kind load docker-image inventro:local --name inventro-local

# 3) Apply manifests
kubectl apply -n inventro -f k8s/configmap.yaml
kubectl apply -n inventro -f k8s/secrets.yaml
kubectl apply -n inventro -f k8s/pvc.yaml
kubectl apply -n inventro -f k8s/postgres-deployment.yaml
kubectl apply -n inventro -f k8s/deployment.yaml
kubectl apply -n inventro -f k8s/cronjob-backup.yaml

# 4) Smoke checks
kubectl get pods -n inventro -w
kubectl logs -n inventro deploy/inventro-deployment --tail=100

# 5) Port-forward to app (adjust service/port if needed)
kubectl port-forward -n inventro svc/inventro-service 8000:8000
# Visit http://localhost:8000

# 6) Optional: migrations
kubectl exec -n inventro deploy/inventro-deployment -- python manage.py migrate

# 7) Tear down
kind delete cluster --name inventro-local
```

## Option B: Minikube
```bash
# 1) Start cluster + namespace
minikube start --driver=docker
kubectl create namespace inventro

# 2) Use in-cluster Docker daemon to avoid pushing images
eval $(minikube docker-env)
docker build -t inventro:local .

# 3) Apply manifests (no kind load needed)
kubectl apply -n inventro -f k8s/configmap.yaml
kubectl apply -n inventro -f k8s/secrets.yaml
kubectl apply -n inventro -f k8s/pvc.yaml
kubectl apply -n inventro -f k8s/postgres-deployment.yaml
kubectl apply -n inventro -f k8s/deployment.yaml
kubectl apply -n inventro -f k8s/cronjob-backup.yaml

# 4) Smoke checks
kubectl get pods -n inventro -w
kubectl logs -n inventro deploy/inventro-deployment --tail=100

# 5) Port-forward
kubectl port-forward -n inventro svc/inventro-service 8000:8000

# 6) Optional: migrations
kubectl exec -n inventro deploy/inventro-deployment -- python manage.py migrate

# 7) Tear down
minikube delete
```

## Quick verification checklist
- Pods ready: `kubectl get pods -n inventro`
- Django responsive: open http://localhost:8000 after port-forward
- Logs: no stack traces when loading key pages
- DB: migrations run without errors
