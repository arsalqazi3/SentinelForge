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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest tests/
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'sonar-scanner'
                    withSonarQubeEnv('sonarqube') {
                        sh """
                            echo "SONAR_HOST_URL: \$SONAR_HOST_URL"
                            echo "Token length: \${#SONAR_AUTH_TOKEN}"
                            ${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=sentinelforge -Dsonar.sources=app.py,tests/ -Dsonar.exclusions=venv/**,**/__pycache__/**,*.png
                        """
                    }
                }
            }
        }
    }
}
