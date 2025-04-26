pipeline {
    agent { label 'agent1' }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lauprieto/Python.git'
            }
        }
        stage('Setup Python') {
            steps {
                sh '''
                    command -v python3 || echo "Python3 no está instalado"
                    command -v pip3 || echo "pip3 no está instalado"
                    command -v python3-venv || echo "python3-venv no está instalado"
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }
    }
}
