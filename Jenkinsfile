pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
       stage('Code Quality Check via SonarQube') {
           steps {
                script {
                def scannerHome = tool 'SonarQube';
                withSonarQubeEnv("SonarQube-Server") {
                sh "${scannerHome}/opt/sonar-scanner-4.5/bin/sonar-scanner \
               -Dsonar.projectKey=test-node-js \
               -Dsonar.sources=. \
               -Dsonar.css.node=. \
               -Dsonar.exclusions=vendor/**, storage/**, resources/** \
               -Dsonar.language=py \
               -Dsonar.java.binaries=target/classes \
               -Dsonar.sources=/var/lib/jenkins/workspace/$JOB_NAME \
               -Dsonar.sourceEncoding=UTF-8 \
               -Dsonar.projectName=PythonJenkinsTest \
               -Dsonar.host.url=http:192.168.1.204:9000 \
               -Dsonar.login=admin \
               -Dsonar.password=Admin"
               }
           }
      }
  }
   
}
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
