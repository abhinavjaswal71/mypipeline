pipeline {
  agent any
  stages {
    stage('Development') {
      steps {
        echo 'I am in development stage'
        sh 'git --version'
      }
    }
    stage('Testing') {
      steps {
        echo 'I am in testing stage'
        sh 'docker --version'
      }
    }
    stage('Production') {
      steps {
        echo 'I am in production stage'
        sh 'java --version'
      }
    }
  }
}
