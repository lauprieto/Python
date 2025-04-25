pipeline {
<<<<<<< HEAD
    agent { label 'agent3' }

=======
    agent any
>>>>>>> c42f3da650cfa0dde975df7a044bf986365ae67c
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
