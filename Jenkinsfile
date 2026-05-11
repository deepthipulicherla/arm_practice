pipeline {
    agent any

    stages {

        stage('Setup Python') {
            steps {
                bat '''
                    python --version
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    python run_tests.py jenkins
                '''
            }
        }
    }

    post {
        always {
            echo "Publishing Allure report and archiving artifacts..."
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
        }
        success {
            echo "Build succeeded."
        }
        failure {
            echo "Build failed."
        }
    }
}
