# Summary
- What's docker registry?
  - The Docker registry is docker image storage location.
- What's docker hub?
  - The Docker hub is one of the docker registries
  - The Docker hub has many registory
- What's docker image?
  - The Docker image is the source of a containter.
- docker login
  - Login the docker hub
- docker pull <image>
  - Pull the docker image from docker hub
- docker run -it <images> bash
  - Create docker container from docker image
- exit
  - Stop the process(stop container)
- docker ps -a
  - Show the all docker container(-a:include stop container)
- docker images
  - Show the docker image files
- docker restart
  - Restart the stop docker container
- docker exec -it <container> bash
  - Execute bash process
- docker commit <container> <image>
  - Create from Docker container to Docker image
- docker tag <source> <target>
  - The image name of docker and the registry name must match.
  - So, change the name of the docker image.
- docker push <image>
  - Push the image from local pc to docker hub
- docker rmi <image>
  - Remove docker image from local pc