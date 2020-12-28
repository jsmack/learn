# Instruction
## FROM
- FROM is base Docker image

```
>>> docker build .
Sending build context to Docker daemon  5.632kB
Step 1/2 : FROM ubuntu:latest
 ---> f643c72bc252                   <- ubuntu image IMAGE ID
Step 2/2 : RUN touch test
 ---> Using cache
 ---> aaf7263913df                   <- new layer
Successfully built aaf7263913df
 >>>
 >>> docker images
REPOSITORY           TAG       IMAGE ID       CREATED         SIZE
new-ubuntu           latest    aaf7263913df   6 days ago      72.9MB
ubuntu               updated   dfd323755a9f   2 weeks ago     72.9MB
jsmack/docker-lean   latest    dfd323755a9f   2 weeks ago     72.9MB
ubuntu               latest    f643c72bc252   4 weeks ago     72.9MB   <- ubuntu image IMAGE ID
hello-world          latest    bf756fb1ae65   12 months ago   13.3kB
 >>>
```