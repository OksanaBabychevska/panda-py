pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'temperature_app_image'
        REPO_URL = 'https://github.com/OksanaBabychevska/panda-py.git'
    }

    stages {
        stage('Checkout') {
            steps {
                git REPO_URL
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'docker-compose up -d'
                    def containerId = sh(script: "docker ps -qf \"name=temperature_app\"", returnStdout: true).trim()
                    sh "docker exec ${containerId} python /app/test_app.py"
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.prod.yml up -d'
                }
            }
        }

        stage('Teardown') {
            steps {
                script {
                    sh 'docker-compose down --volumes --remove-orphans'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
