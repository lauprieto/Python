pipeline {
    agent { label 'agent3' }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lauprieto/Python.git'
            }
        }
        stage('Test') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pytest
                '''
            }
        }
    }
}
