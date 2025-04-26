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
                script {
                    // Verificar si Python3 y pip3 están instalados
                    sh '''
                        command -v python3 || echo "Python3 no está instalado"
                        command -v pip3 || echo "pip3 no está instalado"
                        command -v python3-venv || echo "python3-venv no está instalado"
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Crear un entorno virtual, activarlo e instalar dependencias
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
    post {
        always {
            echo 'Pipeline terminado.'
        }
        success {
            echo '¡El pipeline fue exitoso!'
        }
        failure {
            echo 'Hubo un error en el pipeline.'
        }
    }
}
