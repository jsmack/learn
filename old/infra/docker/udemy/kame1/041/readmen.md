# CMD Instruction
## Explanation
- CMD sepecifies the default command for the container
- In principle, write at the end of the Dockerfile
- RUN command only once

## Example
- executable
  - command
```Dockerfile
CMD ["executable", "param1", "param2"]
```

## Take a look at ubuntu Dockerfile
- https://github.com/tianon/docker-brew-ubuntu-core/blob/74249faf47098bef2cedad89696bfd1ed521e019/focal/Dockerfile#L43
```Dockerfile
CMD ["/bin/bash"]
```

## Create Docker file
```Dockerfile
FROM ubuntu:latest

RUN apt-get update &&  \
    apt-get install -y \
    curl \
    cvs  \
    nginx

CMD ["ls"]
```

## Generate docker image
- Using cache
- I have a layer of Docke image that i Created laset time and used them as a cache, so the process finished fast
```bash
>>> docker build .
Sending build context to Docker daemon  4.096kB
Step 1/3 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/3 : RUN apt-get update &&      apt-get install -y     curl     cvs      nginx
 ---> Using cache
 ---> 77823494807f
Step 3/3 : CMD ["ls"]
 ---> Running in 27333c9eec05
Removing intermediate container 27333c9eec05
 ---> c376ff8c991d
 >>>
```

## Execute container
- The ls command is executed
```bash
>>> docker run c376ff8c991d
bin
boot
dev
etc
home
lib
lib32
lib64
libx32
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
```

## Modify Docker file
```Dockerfile
FROM ubuntu:latest

RUN apt-get update &&  \
    apt-get install -y \
    curl \
    cvs  \
    nginx

CMD ["pwd"]
```

## Generate and execute
```
>>> docker build .
Sending build context to Docker daemon  4.608kB
Step 1/3 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/3 : RUN apt-get update &&      apt-get install -y     curl     cvs      nginx
 ---> Using cache
 ---> 77823494807f
Step 3/3 : CMD ["pwd"]
 ---> Running in 2a645f0bb874
Removing intermediate container 2a645f0bb874
 ---> 09360a5574a3
Successfully built 09360a5574a3
>>> docker run 09360a5574a3
/
 >>>
```