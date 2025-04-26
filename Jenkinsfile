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
                apt-get update
                apt-get install -y python3-venv python3-pip
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
