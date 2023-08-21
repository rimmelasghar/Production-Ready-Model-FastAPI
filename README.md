<img src="https://github.com/rimmelasghar/Deploy-ML-FastAPI/blob/main/img/ML.jpg" alt="Girl in a jacket" width="1000" height="250">

# Deploy ML models with FastAPI, Docker, and Google Cloud Run

### 1. Develop and save the model with this Colab

[Open Colab](https://colab.research.google.com/drive/1uaALcaatvxOu42IhQA4r0bahfdpw-Z7v?usp=sharing)

### 2. Create Docker container

create a container by executing the following command.
```bash
docker compose -f "docker-compose.production.yaml" up --build
docker compose -f "docker-compose.production.yaml" up
doc
```

The application will be available at http://0.0.0.0:8000/app/docs/

### 3. Create a Public Repository on Docker Hub.

login or signup to [docker hub](https://hub.docker.com/) and create a empty repository.

<img src="https://github.com/rimmelasghar/Deploy-ML-FastAPI/blob/main/img/dockerhub-repository.jpg" alt="creating a repository on docker hub" width="250" height="250">

### 4. Build a Docker Image and Push it to Docker Hub.

create a docker image by executing the command and push the image to docker hub.

```bash
docker build -t rimmelasghar4/model-deployment-fastapi:1.0.0 .
docker login

```
The command docker build -t rimmelasghar4/model-deployment-fastapi:1.0.0 . is used to build a Docker image based on a Dockerfile in the current directory (.) and tag it with a specific name and version number.

```bash
docker push rimmelasghar4/model-deployment-fastapi:1.0.0
```
The command docker push rimmelasghar4/model-deployment-fastapi:1.0.0 is used to push a Docker image to a container registry, making it available for others to pull and use. 

### 5. Create a Service on Cloud Run (GCP):
head over to [GCP cloud run](https://console.cloud.google.com/run) and create a service.

<img src="https://github.com/rimmelasghar/Deploy-ML-FastAPI/blob/main/img/cloud-run-interface.jpg" alt="creating a service on cloud run" width="250" height="250">

see this tutorial on how to create a service on google cloud run 
[here](https://www.cyberithub.com/how-to-create-service-in-google-cloud-run-using-6-easy-steps/)

some changes to do while creating a service
 - add container url 'model-deployment-fastapi:1.0.0'
 - select port number as 8000(same as mention in docker file)
 - select capacity as 1Gib
 - add environment variable

 click CREATE to create a service

wallah, you've successfully deployed a ml model on cloud run:


<img src="https://github.com/rimmelasghar/Deploy-ML-FastAPI/blob/main/img/cloud-run-created.jpg" alt="creating a service on cloud run" width="250" height="250">

head over to the url

<img src="https://github.com/rimmelasghar/Deploy-ML-FastAPI/blob/main/img/cloud-run-deployed.jpg" alt="creating a service on cloud run" width="250" height="250">