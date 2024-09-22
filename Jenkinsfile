pipeline {
    agent any

    // Git repository configuration
    environment {
        GIT_REPO = 'https://github.com/ourFirstAotganizesuper46/simple-api'
        GIT_REPO_ROBOT = 'https://github.com/ourFirstAotganizesuper46/simple-api-robot'
        IMAGE_NAME = 'ghcr.io/ourfirstaotganizesuper46/simple-api'
    }
    stages {

        stage("Clone simple-api"){
            agent {label "vm2"} 
            steps {
                git branch: "main", url: "${GIT_REPO}"
            }
        }

        stage("Unit Test") {
            agent {label "vm2"} 
            steps {
                sh '/usr/bin/pip3 install -r requirements.txt'
                sh 'python3 -m unit_test -v'
                echo "Unit test done!"
            }
        }

        stage("Create Image/Container") {
            agent {label "vm2"} 
            steps {
                withCredentials(
                    [usernamePassword(
                        credentialsId: 'PAT_github',
                        passwordVariable: 'gitPassword',
                        usernameVariable: 'gitUser'
                    )]
                ){
                    sh "docker login -u ${gitUser} -p ${gitPassword} ghcr.io"
                    sh "docker build -t ${IMAGE_NAME} ./app"
                    sh "docker compose -f docker-compose.yml up -d" 
                    sh "docker ps"
                }
            }
        }

        stage("Clone/Setup Robot"){
            agent {label "vm2"} 
            steps{
                dir('./robot-test/'){
                    git branch: 'main', credentialsId: 'PAT_github', url: '${GIT_REPO_ROBOT}'
                    echo "Clone done!"
                }
            }
        }

        stage("Run Robot") {
            agent {label "vm2"} 
            steps{
                sh "python3 -m robot test-calculate.robot"
            }
        }

        stage("Push Image"){
            agent {label "vm2"} 
            steps{
                withCredentials(
                    [usernamePassword(
                        credentialsId: 'PAT_github',
                        passwordVariable: 'gitPassword',
                        usernameVariable: 'gitUser'
                    )]
                ){
                    sh "docker login -u ${gitUser} -p ${gitPassword} ghcr.io"
                    sh "docker tag ${IMAGE_NAME} ${IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker push ${IMAGE_NAME}"
                    sh "docker push ${IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker rmi -f ${IMAGE_NAME}"
                    sh "docker rmi -f ${IMAGE_NAME}:${env.BUILD_NUMBER}"
                }
            }  
        }

        stage("Compose Down"){
            agent {label "vm2"} 
            steps{
                sh "docker compose -f docker-compose.yml down"
                sh "docker system prune -a -f" 
            }  
        }

        stage("Pull IMGAGE") {
            agent {label "vm3"} //vm3
            steps{
                withCredentials(
                    [usernamePassword(
                        credentialsId: 'PAT_github',
                        passwordVariable: 'gitPassword',
                        usernameVariable: 'gitUser'
                    )]
                ){
                    sh "docker login -u ${gitUser} -p ${gitPassword} ghcr.io"
                    sh "docker pull ${IMAGE_NAME}"
                }
            }
        }

        stage("Pre Prod") {
            agent {label "vm3"} //vm3
            steps{
                echo "Clear VM3 system"
                sh "docker stop \$(docker ps -a -q) || true"
                sh "docker system prune -a -f"


                echo "Creating Container"
                sh "docker compose up -d"
            }
        }
    }
}
