# What does docker run do?
- Generate container from Docker image
- run = create + start

# What's docker run?
- if not docker image in the local pc
  - pull docker images from docker hub
    -  docker pull <image>
- docker craete <image>
- docker start created container
- Execute default command


# What is the hello-world container doing?
- output the text 

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
 $
 ```

 # docker create
 - Create from the Docker image

 ```
$ docker create hello-world
f637867eaca7d0014dab28b85e46d948fe8e38dc3a8e0576fd6e5fff30de174b
$ docker ps -a
CONTAINER ID   IMAGE                       COMMAND    CREATED         STATUS                     PORTS     NAMES
f637867eaca7   hello-world                 "/hello"   6 seconds ago   Created                              peaceful_mcclintock    <- created container
8259beef5e98   hello-world                 "/hello"   2 minutes ago   Exited (0) 2 minutes ago             determined_lovelace
e1d8789ede51   jsmack/docker-lean:latest   "bash"     2 days ago      Exited (0) 2 days ago                bold_lederberg
88e62b113daa   ubuntu:latest               "bash"     4 days ago      Exited (255) 3 days ago              stupefied_margulis
$
```

# docker start
- Start container
- Execute default command

```
$ docker start f637867eaca7
f637867eaca7
$
```

# But, container exited...

```
$ docker ps -a
CONTAINER ID   IMAGE                       COMMAND    CREATED         STATUS                      PORTS     NAMES
f637867eaca7   hello-world                 "/hello"   3 minutes ago   Exited (0) 57 seconds ago             peaceful_mcclintock   <- container status is exited...
8259beef5e98   hello-world                 "/hello"   5 minutes ago   Exited (0) 5 minutes ago              determined_lovelace
e1d8789ede51   jsmack/docker-lean:latest   "bash"     2 days ago      Exited (0) 2 days ago                 bold_lederberg
88e62b113daa   ubuntu:latest               "bash"     4 days ago      Exited (255) 3 days ago               stupefied_margulis
$ 
```

# Why is the text out displayed?
- The docker start command does not show the result of the default execution command.
- But, I want see result of execution command
- Use "-a" option

```
$ docker start f637867eaca7 -a

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
$ 
```

# Default command?
- The Default command is COMMAND
- The default command for hello-world container is /hello
```
$ docker ps -a
CONTAINER ID   IMAGE                       COMMAND    CREATED          STATUS                          PORTS     NAMES
f637867eaca7   hello-world                 "/hello"   21 minutes ago   Exited (0) About a minute ago             peaceful_mcclintock
8259beef5e98   hello-world                 "/hello"   23 minutes ago   Exited (0) 23 minutes ago                 determined_lovelace
e1d8789ede51   jsmack/docker-lean:latest   "bash"     2 days ago       Exited (0) 2 days ago                     bold_lederberg
88e62b113daa   ubuntu:latest               "bash"     4 days ago       Exited (255) 3 days ago                   stupefied_margulis
$
```

# The override default command
- However, there is no bash in the hellow-world container 
```
$ docker run hello-world bash -it
docker: Error response from daemon: OCI runtime create failed: container_linux.go:370: starting container process caused: exec: "bash": executable file not found in $PATH: unknown.
ERRO[0000] error waiting for container: context cancele
$ 
``` 
