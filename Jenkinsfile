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
                    // Cambiar la ruta de creación del entorno virtual
                    bat '''
                    python -m venv C:\\path\\to\\venv
                    C:\\path\\to\\venv\\Scripts\\activate
                    pip install -r requirements.txt
                    pytest
                    '''
                }
            }
        }
    }
}
