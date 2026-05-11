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
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
        }

        success {
            emailext(
                subject: "Jenkins Build Successful - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
Build Successful.

Allure Report:
${env.BUILD_URL}allure
""",
                to: "deepthi1987.p@gmail.com"
            )
        }

        failure {
            emailext(
                subject: "Jenkins Build FAILED - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
Build Failed.

Console Output:
${env.BUILD_URL}console

Allure Report (if generated):
${env.BUILD_URL}allure
""",
                to: "deepthi1987.p@gmail.com"
            )
        }
    }
}
