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
        
        stage('rest_app.py') {
            steps {
                script {
                    sh "pip3 install --user selenium"
                     if (Boolean.valueOf(env.UNIX)) {
                        sh 'start /min python3 rest_app.py'
                     } else {
                        bat 'start /min python3 rest_app.py'
                    }
                }
            }
        }
        stage('web_app.py'){
            steps{
                script{
                    if (Boolean.valueOf(env.UNIX)){
                        sh 'start /min python web_app.py'
                    } else {
                        bat 'start /min python web_app.py'
                    }
                }
            }
        }
        stage('backend_testing.py'){
            steps{
                script{
                    if (Boolean.valueOf(env.UNIX)){
                      sh 'python3 backend_testing.py'
                    } else {
                        bat 'python3 backend_testing.py'
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

