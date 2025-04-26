pipeline {
    agent { label 'agent1' }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lauprieto/Python.git'
            }
        }

        stage('Verificar archivos') {
            steps {
                sh 'ls -la'  // Listar todos los archivos del directorio
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    cd python1
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=report.xml
                '''
            }
            post {
                always {
                    junit 'report.xml'
                }
            }
        }
    }
}