pipeline {
    environment {
        imagename = "ranjitdas977/jenkinspractice"
        registryCredential = "jenkins_docker_hub"
        theDockerFile = 'Dockerfile'
    }
    agent any

    stages {
        stage('Cloning Git') {
            git([url: 'https://github.com/ranjitdas977/jenkinspractice.git', branch:'main', credentialsID: 'jenkin_github_ssh'])
        }
    }
    stage('Building imgae') {
        steps{
            script{
                dockerImage = docker.build imagename
            }
        }
    }
    stage('Deploy Image') {
        steps{
            script {
                docker.withRegistry('', registryCredential) {
                    dockerImage.push("$BUILD_NUMBER")
                    dockerImage.push('latest')
                }
            }
        }
    }
    stage('Remove Unsed docker image') {
        steps{
            sh "docker rmi $imagename:$BUILD_NUMBER"
            sh "docker rmi $imagename:latest"
        }
    }
}
