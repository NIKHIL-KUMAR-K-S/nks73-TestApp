# Setup & Quickstart for devops-starter

## Prerequisites
- GitHub repo (push this scaffold to your repo)
- Jenkins installed locally (Windows/Mac/Linux) for CD
- Codespaces or any k3d/minikube cluster for K8s (or cloud cluster)

## 1. Push to GitHub
git init
git add .
git commit -m "Initial commit: devops-starter scaffold"
git branch -M main
git remote add origin https://github.com/NIKHIL-KUMAR-K-S/devops-starter-devops.git
git push -u origin main

## 2. GitHub Actions
- Workflow located at `.github/workflows/build-and-push.yml`
- On push to main, Actions builds and pushes image to GHCR:
  `ghcr.io/NIKHIL-KUMAR-K-S/devops-starter:<commit-sha>`

## 3. Jenkins
- Add a Secret File credential with ID `kubeconfig-dev` containing kubeconfig for your cluster
- Create Pipeline job pointing at this repo (Jenkinsfile). Provide parameter `IMAGE_TAG` when triggering.
- Trigger build with IMAGE_TAG=<commit-sha> to deploy via Helm.

## 4. Run cluster (Codespaces/k3d)
- In Codespaces: install k3d and create a cluster:
  `k3d cluster create devcluster`
- Then run:
  `helm upgrade --install devops-starter helm-chart -n dev --set image.repository=ghcr.io/NIKHIL-KUMAR-K-S/devops-starter --set image.tag=<commit-sha>`
