pipeline {
    agent { label 'agent1' }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lauprieto/Java.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest'
            }
            post {
                always {
                    junit '**/tests/test_*.xml'
                }
            }
        }
    }
}
