#  Prepare upload to docker hub
- defaults
  - \<hostname\>:\<port\>/\<username\>/\<repository\>:\<tag\>
    - \<hostname\>:\<port\> : registry-1.docker.io
    - \<username\>: library
    - \<tag\>: latest
    - registry-1.docker.io/library/ubuntu:latest

- Change image name
```
$ docker tag source target
$ docker tag ubuntu:updated username/docker-lean
```

- update
  - Create new images
  - Same IMAGE ID ubuntu:updated and xxxxxx/docker-lean
```
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
ubuntu        updated   dfd323755a9f   15 minutes ago   72.9MB
ubuntu        latest    f643c72bc252   2 weeks ago      72.9MB
hello-world   latest    bf756fb1ae65   11 months ago    13.3kB
$
$ docker tag ubuntu:updated  xxxxxx/docker-lean
$
$docker images
REPOSITORY           TAG       IMAGE ID       CREATED          SIZE
xxxxxx/docker-lean   latest    dfd323755a9f   57 minutes ago   72.9MB
ubuntu               updated   dfd323755a9f   57 minutes ago   72.9MB
ubuntu               latest    f643c72bc252   2 weeks ago      72.9MB
hello-world          latest    bf756fb1ae65   11 months ago    13.3kB
$
```