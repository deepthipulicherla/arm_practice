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

        stage('Publish Allure Report') {
            when {
                always()
            }
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }

        stage('Archive Allure Report') {
            when {
                always()
            }
            steps {
                archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
                archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
            }
        }
    }

    post {
        always {
            echo "Build finished. Allure report archived."
        }
        success {
            echo "Build succeeded."
        }
        failure {
            echo "Build failed."
        }
    }
}
