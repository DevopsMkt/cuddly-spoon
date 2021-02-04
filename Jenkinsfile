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
                def scannerHome = tool 'sonarqube';
                withSonarQubeEnv("sonarqube-container") {
17
           sh "${tool("sonarqube")}/bin/sonar-scanner \
18
           -Dsonar.projectKey=test-node-js \
19
           -Dsonar.sources=. \
20
           -Dsonar.css.node=. \
21
           -Dsonar.host.url=http://your-ip-here:9000 \
22
           -Dsonar.login=your-generated-token-from-sonarqube-container"
23
               }
24
           }
25
       }
26
   }
        
        stage('SonarQube Analysis') {
            step {
                sh '${scannerHome}/opt/sonar-scanner-4.5/bin/sonar-scanner -Dsonar.host.url=http://192.168.1.204:9000 -Dsonar.projectName=meanstackapp1 -Dsonar.projectVersion=1.1 -Dsonar.projectKey=meanstack1:app -Dsonar.projectBaseDir=/var/lib/jenkins/workspace/SonarQube-Test-Pipeline1 '
    
    
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
