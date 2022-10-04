**Django ELK Sample App**
Please follow the steps for app installation

---

## Set docker credenatials for kubernetes cluster 
```
kubectl create secret docker-registry docker-keys \
   --docker-username=<docker username> \
   --docker-password=<password> \
   --docker-email=<personal email> \
   --docker-server=https://index.docker.io/v2/
```

## Create Docker images
Create app docker image
```
cd <Path to project>\django-elk\django_elk
docker build -t sanidhya/django_elk:app-20221004_1 -f .\Dockerfile.prod .
docker push sanidhya/django_elk:app-20221004_1
```

Create Nginx docker image
```
cd <Path to project>\django-elk\nginx
docker build -t sanidhya/django_elk:nginx-20221004_1 -f .\Dockerfile.prod .
docker push sanidhya/django_elk:nginx-20221004_1
```

Deploy application in Kubernetes
```
cd <Path to project>\django-elk\k8s
# Deploy elasticsearch pods
kubectl apply -f elastic-deployment.yml
# Check for pods to start 
kubectl get po
# Deploy service 
kubectl apply -f elastic-service.yml
# Deploy web app pods
kubectl apply -f webapp-deployment.yml
# Check for pods to start 
kubectl get po
# Deploy service 
kubectl apply -f app-service.yml
# Port forward to access the application web ui
kubectl port-forward service/app-service 7080:80
```

To try the local setup using docker-compose
```
cd <Path to project>
docker compose -f docker-compose.qa.yml up --build -d
```
---
