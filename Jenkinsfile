pipeline {
  agent any
  stages {
    stage('Dev') {
      steps {
        echo 'I am in development stage'
        sh 'git --version'
      }
    }
    stage('Test') {
      steps {
        echo 'I am in test'
        sh 'python --version'
      }
    }
    stage('Prod') {
      steps {
        echo 'I am in prod'
        sh 'node --version'
      }
    }
  }
}
