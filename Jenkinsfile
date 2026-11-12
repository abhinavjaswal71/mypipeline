pipeline {
  agent any
  stages {
   
    stage('Docker Build') {
      steps {
        echo 'I am in Docker Build Stage'
        sh 'docker build -t myapp:latest .'
      }
    }
    stage('Docker Run') {
      steps {
        echo 'Running Docker Container'
        sh 'docker run -d -p 8080:8000 myapp:latest'
      }
    }
  }
}
