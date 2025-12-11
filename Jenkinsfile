pipeline {
  agent any
  parameters {
    string(name: 'IMAGE_TAG', defaultValue: '', description: 'Image tag or SHA to deploy (required)')
  }
  environment {
    IMAGE_REPO = "ghcr.io/NIKHIL-KUMAR-K-S/devops-starter"
    K8S_NAMESPACE = "dev"
    KUBECONFIG_CREDENTIAL_ID = "kubeconfig-dev"
  }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Deploy (Helm)') {
      steps {
        script { if (!params.IMAGE_TAG) { error "IMAGE_TAG parameter is required" } }
        withCredentials([file(credentialsId: env.KUBECONFIG_CREDENTIAL_ID, variable: 'KUBECONFIG_FILE')]) {
          sh '''
            export KUBECONFIG=${KUBECONFIG_FILE}
            helm repo update || true
            helm upgrade --install devops-starter helm-chart -n ${K8S_NAMESPACE} --create-namespace \
              --set image.repository=${IMAGE_REPO} --set image.tag=${IMAGE_TAG}
          '''
        }
      }
    }
  }
  post {
    success { echo "Deployed ${IMAGE_REPO}:${params.IMAGE_TAG}" }
    failure { echo "Deployment failed" }
  }
}
