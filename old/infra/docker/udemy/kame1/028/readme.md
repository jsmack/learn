# Detached mode
- docker run -d <image>
  - After starting the container, return to bash immediately.
  - Execute background
```
$ docker run -it -d ubuntu bash
e711879a9f1a337e5d08feb5e3aefe9745fc3ee12276f8a6d01a02b8572f14c3
$
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                      PORTS     NAMES
e711879a9f1a   ubuntu    "bash"        4 seconds ago    Up 3 seconds                          cranky_gagarin
$
```



# Foreground mode
- docker run --rm <image>
  - one-time container
  - --rm
    - Delete the container immedeiately after stopping it.
```
$ docker run --rm hello-world

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
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS         PORTS     NAMES
e711879a9f1a   ubuntu    "bash"    2 minutes ago   Up 2 minutes             cranky_gagarin
$ 
```