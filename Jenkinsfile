pipeline {
    environment {
        registryCredential = 'dockerhub'
    }
    agent any
    stages {
        stage('Lint: HTML Check') {
            steps {
                sh 'tidy -q -e templates/*.html'
            }
        }
        stage('Build Docker Image') {
          steps {
            sh "./docker_build.sh"
          }
        }
        stage('Deploy Docker Image') {
            steps {
                sh "kubectl set image deployment/timemachine-deployment timemachine=y3key/timemachine-kube:${env.GIT_COMMIT[0..7]}"
            }
        }
    }
}
