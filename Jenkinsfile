
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                bat '''
                    "%PYTHON%" --version
                    "%PYTHON%" -m venv .venv
                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat '.venv\\Scripts\\python.exe monitor.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hello-jenkins-monitoring .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --rm hello-jenkins-monitoring'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'evidently_report.html',
                             allowEmptyArchive: true
        }
    }
}
