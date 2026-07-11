pipeline {
    agent any

    environment {
        REPO = 'https://github.com/vishnuvardhanpatta-ux/docker-compose-cicd.git'
    }

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${REPO}"
            }
        }

        stage('Stop Existing Containers') {
            steps {
                bat 'docker compose down'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Deploy Application') {
            steps {
                bat 'docker compose up -d'
            }
        }

        stage('Wait for Application') {
            steps {
                bat 'timeout /t 10 /nobreak'
            }
        }

        stage('Health Check') {
            steps {
                bat 'curl --fail http://localhost:5000/health'
            }
        }

    }

    post {

        success {
            echo 'Deployment Successful!'
            echo 'Application is running successfully.'
        }

        failure {
            echo 'Deployment Failed!'
            echo 'Displaying container logs...'

            bat 'docker ps -a'
            bat 'docker logs flask_app'
        }

        always {
            echo 'Pipeline Execution Completed.'
        }
    }
}