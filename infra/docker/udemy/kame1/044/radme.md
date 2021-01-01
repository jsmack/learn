# What is docker build doing
## Why specify the current directory instead of specifying the Dockerfile
- The docker build command passes the directory to the docker daemon
- The docker daemon is generate an image based on the directory and Dockerfile
- This Directory is called the build context

## Command
```Dockerfile
>>> docker build .
Sending build context to Docker daemon  3.584kB       <- Attention here
Step 1/3 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/3 : RUN apt-get update &&      apt-get install -y     curl     cvs      nginx &&     apt-get clean &&     rm -rf /var/lib/apt/lists/*
 ---> Using cache
 ---> ca3f82001404
Step 3/3 : CMD ["pwd"]
 ---> Using cache
 ---> 589a57a51c96
Successfully built 589a57a51c96
>>>
```
## Why docker build use build context
- The docker build command can import files that are in the build context