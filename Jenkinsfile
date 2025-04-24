pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lauprieto/Python.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
    }
}
