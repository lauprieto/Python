pipeline {
    agent { label 'agent1' }

    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/lauprieto/Python.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt || true'
            }
        }

        stage('Ejecutar script') {
            steps {
                sh './venv/bin/python main.py'
            }
        }

        stage('Pruebas') {
            steps {
                sh './venv/bin/python -m unittest discover -s test'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado.'
        }
    }
}
