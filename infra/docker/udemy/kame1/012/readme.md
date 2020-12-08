- Check runninng container
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

- Check docker image in local computer
```
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              bf756fb1ae65        11 months ago       13.3kB
```

- Start the hello-world container
```
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

- Show all container
  - Generates a random name if NAME is not specified
```
docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
5f9058f3b341        hello-world         "/hello"            2 minutes ago       Exited (0) 2 minutes ago                       funny_easley
```

- Show active container
```
docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
```

- What is the Docker run(hello-world image)?
1. Run
2. Create container from docker image
3. Execute command
4. Exit

