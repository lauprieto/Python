pipeline {
    agent { label 'agent1' }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lauprieto/Python.git'
            }
        }

        stage('Test') {
            steps {
                script {
                    // Ejecutar el entorno virtual en Windows
                    bat '''
                    python -m venv venv
                    venv\\Scripts\\activate
                    pip install -r requirements.txt
                    pytest
                    '''
                }
            }
        }
    }
}
