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
                script {
                    dockerImage = docker.build("y3key/timemachine-kube:${env.GIT_COMMIT[0..7]}")
                    docker.withRegistry('', registryCredential) {
                          dockerImage.push()
                    }
                }
                               
            }
        }  
        stage('Deploy Docker Image') {
            steps {
                withAWS(credentials: 'aws-credentials', region: 'us-east-1') {
                    sh "kubectl set image deployment/timemachine-deployment timemachine=y3key/timemachine-kube:${env.GIT_COMMIT[0..7]}"
                }
            }
        }
    }
}
