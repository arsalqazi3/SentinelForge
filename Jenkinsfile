pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Checkout completed successfully.'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest tests/'
            }
        }
    }
}
