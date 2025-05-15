pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t jenkins-flask-app:latest .'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    bat 'docker run --rm jenkins-flask-app:latest pytest -v'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    bat 'docker stop jenkins-flask-app || exit 0'
                    bat 'docker rm jenkins-flask-app || exit 0'
                    bat 'docker run -d -p 3000:5000 --name jenkins-flask-app jenkins-flask-app:latest'
                    
                    // Check if container is running
                    bat 'docker ps | findstr jenkins-flask-app'
                    
                    echo 'Access your Flask app at http://localhost:3000'
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline succeeded! Flask app running at http://localhost:3000'
        }
        failure {
            echo 'Pipeline failed!'
            bat 'docker stop jenkins-flask-app || exit 0'
            bat 'docker rm jenkins-flask-app || exit 0'
        }
    }
}