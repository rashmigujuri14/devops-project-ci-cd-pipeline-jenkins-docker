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


        stage('Test Application') {
            steps {
                sh '''
                docker rm -f test-container || true

                docker run -d --name test-container -p 5001:5000 flask-jenkins-app

                sleep 5

                curl localhost:5001

                docker stop test-container
                docker rm test-container
                '''
            }
        }


        stage('Deploy Container') {
            steps {
                sh '''
                docker rm -f flask-container || true

                docker run -d \
                --name flask-container \
                -p 5000:5000 \
                flask-jenkins-app
                '''
            }
        }


        stage('Cleanup') {
            steps {
                sh '''
                docker image prune -f
                '''
            }
        }
    }


    post {

        success {
            echo 'CI/CD Pipeline Completed Successfully 🚀'
        }

        failure {
            echo 'Pipeline Failed ❌'
        }

    }
}
