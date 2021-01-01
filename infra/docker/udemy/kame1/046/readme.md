# What is the docker context?
- Context is environment, status
- File not used for build  cannot be included in the build context
- You can bring the file in the build context to the image with ADD or COPY


# Put a huge file in the build context and buid it
```bash
>>>  dd if=/dev/zero of=./tempfile bs=1024 count=1000000
>>> du -sh tempfile
992M	tempfile
```

```bash
>>> cat Dockerfile
FROM ubuntu:latest

RUN apt-get update \
&&  apt-get install -y\
    curl \
    cvs \
    nginx \
&&  apt-get clean \
&&  rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
>>>
```

- Notice that files not listed in the Dockerfile are being transferred
```
Sending build context to Docker daemon  1.024GB
```

```bash
>>> docker build .
Sending build context to Docker daemon  1.024GB
Step 1/3 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/3 : RUN apt-get update &&  apt-get install -y    curl     cvs     nginx &&  apt-get clean &&  rm -rf /var/lib/apt/lists/*
 ---> Using cache
 ---> 6683b7387c02
Step 3/3 : CMD ["/bin/bash"]
 ---> Using cache
 ---> c4db74553290
Successfully built c4db74553290
>>> 
```

- But not included docker image
```bash
>>> docker images -f dangling=true
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
<none>       <none>    c4db74553290   11 minutes ago   149MB
>>>
```

- If you wan yo include the file in the image, write an ADD or COPY instruction