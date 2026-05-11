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
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
            post {
                always {
                    echo "Allure report published (even if tests failed)."
                }
            }
        }

        stage('Archive Allure Report') {
            steps {
                archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
                archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
            }
            post {
                always {
                    echo "Allure artifacts archived."
                }
            }
        }
    }

    post {
        always {
            echo "Build finished."
        }
        success {
            echo "Build succeeded."
        }
        failure {
            echo "Build failed."
        }
    }
}
