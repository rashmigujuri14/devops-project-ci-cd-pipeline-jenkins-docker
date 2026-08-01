pipeline {
    agent any

    stages {
        stage('Git Check') {
            steps {
                sh 'git --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-jenkins-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f flask-container || true
                docker run -d --name flask-container -p 5000:5000 flask-jenkins-app
                '''
            }
        }
    }
}
