# devops-starter — DevOps Starter Scaffold

This scaffold provides a minimal end-to-end DevOps setup that works without Docker Desktop on your laptop.
It uses:
- GitHub Actions for CI (build & push image to GHCR)
- Jenkins for CD (Helm deploy)
- Helm chart for Kubernetes manifests
- Codespaces / k3d or any kubeconfig-compatible cluster for running Kubernetes

Image repo: `ghcr.io/NIKHIL-KUMAR-K-S/devops-starter`
