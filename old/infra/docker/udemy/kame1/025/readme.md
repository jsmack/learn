# Remove contaier
- remove container
  - docker rm <container>
- stop container
  - docker stop <container>
- All remove container
  - docker system prune
  


- view container list
```
$ docker ps -a
CONTAINER ID   IMAGE                       COMMAND       CREATED          STATUS                        PORTS     NAMES
4f88bf822da3   ubuntu                      "bash"        18 minutes ago   Exited (0) 17 minutes ago               sleepy_murdock
9ed42d4638aa   ubuntu                      "bash"        22 minutes ago   Exited (130) 18 minutes ago             fervent_ellis
1711b5971245   ubuntu                      "ls"          27 minutes ago   Exited (0) 27 minutes ago               confident_haibt
482876b24729   ubuntu                      "/bin/bash"   27 minutes ago   Exited (0) 27 minutes ago               elegant_murdock
9f2cdf848383   ubuntu                      "-it"         28 minutes ago   Created                                 quirky_goldstine
2d5d8cc730c9   ubuntu                      "bash"        29 minutes ago   Exited (0) 29 minutes ago               naughty_kare
aecbd3667608   hello-world                 "bash -it"    3 days ago       Created                                 priceless_easley
f637867eaca7   hello-world                 "/hello"      3 days ago       Exited (0) 3 days ago                   peaceful_mcclintock
8259beef5e98   hello-world                 "/hello"      3 days ago       Exited (0) 3 days ago                   determined_lovelace
e1d8789ede51   jsmack/docker-lean:latest   "bash"        5 days ago       Exited (0) 5 days ago                   bold_lederberg
88e62b113daa   ubuntu:latest               "bash"        7 days ago       Exited (255) 7 days ago                 stupefied_margulis
$ 
```

- Remove container 
```
$ docker rm sleepy_murdock
sleepy_murdock
$
```

- Container with status up connot be deleted
```
$ docker rm nice_visvesvaraya
Error response from daemon: You cannot remove a running container 5ddb9b7bb22e2c2f1834bcf92abbd54e13aa1ac7a0fd08887dfdad28080a6a14. Stop the container before attempting removal or force remove
$
```

- Stop container
```
$ docker stop nice_visvesvaraya
nice_visvesvaraya
$
```

- Container with status exited con be deleted
```
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
$
```