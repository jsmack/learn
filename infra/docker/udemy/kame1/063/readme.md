# Create Dockerfile ds environment

- Dockerfile
```Dockerfile
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim

WORKDIR /opt

RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
RUN 

```

```bash
>>> docker build .
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/4 : RUN apt-get update && apt-get install -y     sudo     wget     vim
 ---> Using cache
 ---> 1370e43890e8
Step 3/4 : WORKDIR /opt
 ---> Using cache
 ---> 1ff565a55995

- snip -

 541450K .......... .......... .......... .......... .......... 99% 36.9M 0s
541500K .......... .......... .......... ........             100% 53.9M=2m10s

2021-01-06 13:12:51 (4.06 MB/s) - 'Anaconda3-2020.11-Linux-x86_64.sh' saved [554535580/554535580]

Removing intermediate container ce9ddd75efe6
 ---> 66709d3e3c70
Successfully built 66709d3e3c70
>>>
```