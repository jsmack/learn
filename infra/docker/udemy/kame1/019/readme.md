# Pull docker images and run container

- Check images(before remove image)
```
$ docker images
REPOSITORY           TAG       IMAGE ID       CREATED         SIZE
xxxxx/docker-lean   latest    dfd323755a9f   34 hours ago    72.9MB
ubuntu               updated   dfd323755a9f   34 hours ago    72.9MB
ubuntu               latest    f643c72bc252   2 weeks ago     72.9MB
hello-world          latest    bf756fb1ae65   11 months ago   13.3kB
$
```
- Remove image in local pc
```
$ docker rmi xxxxx/docker-lean
Untagged: xxxxx/docker-lean:latest
Untagged: xxxxx/docker-lean@sha256:1f55f04dfc0fef840f45a9c45cdfb54386da2ed33701301c7f4fde6c3fe94f86
$
```
- Check images(after remove image)
```
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
ubuntu        updated   dfd323755a9f   34 hours ago    72.9MB
ubuntu        latest    f643c72bc252   2 weeks ago     72.9MB
hello-world   latest    bf756fb1ae65   11 months ago   13.3kB
$
```
- Pull image
```

>>≻ docker pull xxxxx/docker-lean:latest
latest: Pulling from xxxxx/docker-lean
Digest: sha256:1f55f04dfc0fef840f45a9c45cdfb54386da2ed33701301c7f4fde6c3fe94f86
Status: Downloaded newer image for xxxxx/docker-lean:latest
docker.io/xxxxx/docker-lean:latest
```
- Check images(after pull image)
```
$ docker images
REPOSITORY           TAG       IMAGE ID       CREATED         SIZE
xxxxx/docker-lean   latest    dfd323755a9f   34 hours ago    72.9MB
ubuntu               updated   dfd323755a9f   34 hours ago    72.9MB
ubuntu               latest    f643c72bc252   2 weeks ago     72.9MB
hello-world          latest    bf756fb1ae65   11 months ago   13.3kB
$ 
```

- Run containter
```
$ docker run -it xxxxx/docker-lean:latest bash
root@e1d8789ede51:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  test  tmp  usr  var
root@e1d8789ede51:/#
```