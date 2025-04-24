pipeline {
  agent any
  environment {
    REMOTE_USER = 'xm1k'
    REMOTE_HOST = '192.168.0.20'
    REMOTE_DIR  = '/home/xm1k/JenkinsCICD'
    CRED_ID     = '474f7639-1861-4ee5-b337-7346c65d2dab'  // твои SSH-credentials
  }
  stages {
    stage('Clean remote dir') {
      steps {
        sshagent([env.CRED_ID]) {
          sh """
            ssh -o StrictHostKeyChecking=no ${env.REMOTE_USER}@${env.REMOTE_HOST} '
              rm -rf "${env.REMOTE_DIR}"
            '
          """
        }
      }
    }

    stage('Copy repo to remote') {
      steps {
        sshagent([env.CRED_ID]) {
          sh """
            ssh -o StrictHostKeyChecking=no ${env.REMOTE_USER}@${env.REMOTE_HOST} '
              git clone https://github.com/xm1k/JenkinsCICD "${REMOTE_DIR}/"
            '
          """
        }
      }
    }


    stage('Run pytest on remote') {
      steps {
        sshagent([env.CRED_ID]) {
          sh """
            ssh -o StrictHostKeyChecking=no ${env.REMOTE_USER}@${env.REMOTE_HOST} '
              cd "${env.REMOTE_DIR}" &&
              python3 -m pytest --maxfail=1 --disable-warnings -q
             '
          """
        }
      }
    }


    stage('Deploy container if tests passed') {
      steps {
        sshagent([env.CRED_ID]) {
          sh """
            ssh -o StrictHostKeyChecking=no ${env.REMOTE_USER}@${env.REMOTE_HOST} '
              cd "${env.REMOTE_DIR}" &&
    
              # Удаляем старый контейнер (игнорируем ошибку, если его нет)
              docker rm -f myflaskapp || true &&
    
              # Собираем образ
              docker build -t myflaskapp:latest . &&
    
              # Запускаем новый контейнер на порту 5000
              docker run -d --name myflaskapp -p 5000:5000 myflaskapp:latest
            '
          """
        }
      }
    }
}

  post {
    failure {
      echo 'Что-то пошло не так. Проверь логи билдов и ошибки тестов.'
    }
  }
}

