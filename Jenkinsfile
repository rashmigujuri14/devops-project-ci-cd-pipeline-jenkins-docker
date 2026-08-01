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
