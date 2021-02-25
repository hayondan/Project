pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/hayondan/Project_1.git'
            }
        }
        stage('run python rest_app.py') {
            steps {
                script {
                     if (Boolean.valueOf(env.UNIX)) {
                        sh 'python rest_app.py'
                     } else {
                        bat 'python rest_app.py'
                    }
                }
            }
        }
        stage('web_app.py'){
            steps{
                script{
                    if (Boolean.valueOf(env.UNIX)){
                        sh 'web_app.py'
                    } else {
                        bat 'web_app.py'
                    }
                }
            }
        }
        stage('backend_testing.py'){
            steps{
                script{
                    if (Boolean.valueOf(env.UNIX)){
                      sh 'backend_testing.py'
                    } else {
                        bat 'backend_testing.py'
                    }
                }
            }
        }
        stage('frontend_testing.py'){
            steps{
                script{
                if (Boolean.valueOf(env.UNIX)){
                    sh 'frontend_testing.py'
                } else {
                    bat 'frontend_testing.py'
                    }
                }
            }
        }
        stage('combined_testing.py'){
            steps{
                script{
                if (Boolean.valueOf(env.UNIX)){
                    sh 'combined_testing.py'
                } else {
                    bat 'combined_testing.py'
                }
            }
        }
        stage('clean_enviroment.py'){
            steps{
                script{
                if (Boolean.valueOf(env.UNIX)){
                    sh 'clean_enviroment.py'
                } else {
                    bat 'clean_enviroment.py'
                    }
                }
            }
        }
    }
}
}
