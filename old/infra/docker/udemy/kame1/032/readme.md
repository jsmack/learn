# Write Dockerfile

```
# FROM is base image
FROM ubuntu:latest

# Execute command(instruction)
RUN touch test
```

# Generate Docker image from Dockerfime

- build
  1. Move to the directory where the Dockerfile is located
  2. Execute command
     1. docker build .
        1. . is current directory

```
$ docker build .
Sending build context to Docker daemon  3.584kB
Step 1/2 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/2 : RUN touch test
 ---> Running in f0abc10814d3
Removing intermediate container f0abc10814d3
 ---> aaf7263913df
Successfully built aaf7263913df
$
```

- Check image
  - Since the tag name was not specified, the tag name is none.
  - The tag name none is dangling image
    - The dangling image is temporary image 
```
docker images
REPOSITORY           TAG       IMAGE ID       CREATED          SIZE
<none>               <none>    aaf7263913df   32 seconds ago   72.9MB      <- create image
jsmack/docker-lean   latest    dfd323755a9f   8 days ago       72.9MB
ubuntu               updated   dfd323755a9f   8 days ago       72.9MB
ubuntu               latest    f643c72bc252   3 weeks ago      72.9MB
hello-world          latest    bf756fb1ae65   11 months ago    13.3kB
``` 

- Show only dangling images
```
$ docker images -f dangling=true
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
<none>       <none>    aaf7263913df   10 minutes ago   72.9MB
```

- Executed build by specifying the tag name
```
$ docker build -t new-ubuntu:latest .
Sending build context to Docker daemon  4.096kB
Step 1/2 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/2 : RUN touch test
 ---> Using cache
 ---> aaf7263913df
Successfully built aaf7263913df
Successfully tagged new-ubuntu:latest
$
$ docker images
REPOSITORY           TAG       IMAGE ID       CREATED          SIZE
new-ubuntu           latest    aaf7263913df   15 minutes ago   72.9MB
jsmack/docker-lean   latest    dfd323755a9f   8 days ago       72.9MB
ubuntu               updated   dfd323755a9f   8 days ago       72.9MB
ubuntu               latest    f643c72bc252   3 weeks ago      72.9MB
hello-world          latest    bf756fb1ae65   11 months ago    13.3kB
```
