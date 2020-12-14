```
$ docker restart stupefied_margulis
```

```
$ docker exec -it stupefied_margulis bash
root@88e62b113daa:/# exit
exit
$
```

- Save container
  - 88e62b113daa
    - Container ID(docker ps -a)
  - ubuntu
    - image name
  - updated
    - tag name
```
$ docker commit 88e62b113daa ubuntu:updated
sha256:dfd323755a9fd7b66fd382c057aa90bd6a360270d103d1efca2c4f2a3108101b
```

- Check created image
```
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
ubuntu        updated   dfd323755a9f   15 minutes ago   72.9MB    <- create container
ubuntu        latest    f643c72bc252   2 weeks ago      72.9MB
hello-world   latest    bf756fb1ae65   11 months ago    13.3kB
$```

