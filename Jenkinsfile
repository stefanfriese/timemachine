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
                sh "./docker_deploy.sh"
            }
        }
    }
}
