pipeline{
    agent { label 'iac'}
    parameters {
  string defaultValue: 's3://nomedobuck/config', description: '', name: 'S3_URL', trim: true
    }
    stages{
        stage('Checkout'){
            steps{
                checkout scm
            }
        }
        stage('Build image'){
            steps{
                withCredentials([string(credentialsId: 'access_token_key', variable: 'TOKEN_KEY'), string(credentialsId: 'access_token_secret', variable: 'TOKEN_SECRET'), string(credentialsId: 'consumer_key', variable: 'CONSUMER_KEY'), string(credentialsId: 'consumer_secret', variable: 'CONSUMER_SECRET')]) {
                    script{
                        def imagem = docker.build("laudelino100/itau:${env.BUILD_ID}", "--build-arg consumer_key=$CONSUMER_KEY --build-arg consumer_secret=$CONSUMER_SECRET --build-arg token_key=$TOKEN_KEY --build-arg token_secret=$TOKEN_SECRET")
                        imagem.push('latest')
                    }
                }
            }
        }
        stage('Deploy'){
            steps{
                sh 'aws s3 ${params.S3_URL} ~/.kube/config'
                sh 'kubectl create -f deploy.yml'
            }
        }
    }
}