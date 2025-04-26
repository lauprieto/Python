pipeline {
    agent {
        docker { image 'python:3.10' }
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lauprieto/Python.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest --junitxml=report.xml'
            }
            post {
                always {
                    junit 'report.xml'
                }
            }
        }
    }
}
