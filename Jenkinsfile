pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat 'python monitor.py'
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
