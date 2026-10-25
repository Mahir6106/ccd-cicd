pipeline {
    agent any

    environment {
        IMAGE_NAME = 'mahir6106/student-service'
        KUBECONFIG = '/var/lib/jenkins/.kube/config'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }

        stage('Smoke Test') {
            steps {
                sh '''
                    set -e
                    NAME=student-service-test-${BUILD_NUMBER}
                    docker rm -f "$NAME" >/dev/null 2>&1 || true
                    docker run -d --name "$NAME" -p 5001:5000 ${IMAGE_NAME}:${BUILD_NUMBER}
                    trap 'docker rm -f "$NAME" >/dev/null 2>&1 || true' EXIT

                    for i in $(seq 1 15); do
                        if curl -fsS http://127.0.0.1:5001/ >/dev/null; then
                            break
                        fi
                        sleep 2
                    done

                    curl -fsS http://127.0.0.1:5001/
                    curl -fsS http://127.0.0.1:5001/student
                '''
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${IMAGE_NAME}:${BUILD_NUMBER}
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                sh '''
                    kubectl apply -f k8s/deployment.yaml
                    kubectl set image deployment/student-service student-service=${IMAGE_NAME}:${BUILD_NUMBER}
                    kubectl apply -f k8s/service.yaml
                    kubectl rollout status deployment/student-service --timeout=180s
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    kubectl get pods
                    kubectl get deployment student-service
                    kubectl get service student-service
                '''
            }
        }
    }
}


