# Give the container a name
- $ docker run --name <name> ubuntu
- Why give the container a name?
  - Keep starting the container
  - Shared server
  - When accessed from other programs

```
$ docker run --name sample_container ubuntu
$ 
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                      PORTS     NAMES
f73196af7861   ubuntu    "/bin/bash"   34 seconds ago   Exited (0) 33 seconds ago             sample_container
$
```

- Not allowed duplicate container name
```
$ docker run --name sample_container ubuntu
docker: Error response from daemon: Conflict. The container name "/sample_container" is already in use by container "f73196af786169ab598faf2be309717762936bde1a827d820b91769a4eb977de". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
```