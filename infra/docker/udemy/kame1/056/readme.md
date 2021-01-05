# How to control acces to the host file
- Specify u option at run
  - `-u <user_id>:<group_id>`


## TEST
- Dockerfile
```Dockerfile
FROM ubuntu:latest
RUN mkdir /create_in_Dockerfile
```

- build and run
  - `I have no name!`
    - Not exist specific user id in the container
```bash
>>> docker build .
Sending build context to Docker daemon   5.12kB
Step 1/2 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/2 : RUN mkdir /create_in_Dockerfile
 ---> Using cache
 ---> 6f5e7142565e
Successfully built 6f5e7142565e
>>> docker run -it --rm -v /xx/bb/zz/host_dir:/create_in_run -u  $(id -u):$(id -g) 6f5e7142565e bash
I have no name!@c25f16a4f1a6:/$ 
I have no name!@c25f16a4f1a6:/$ ls -ld /create_in_*
drwxr-xr-x 2 root root    4096 Jan  4 08:50 /create_in_Dockerfile
drwxr-xr-x 3  501 dialout   96 Jan  4 08:55 /create_in_run
I have no name!@c25f16a4f1a6:/$
I have no name!@c25f16a4f1a6:/$ touch /create_in_Dockerfile/hoge
touch: cannot touch '/create_in_Dockerfile/hoge': Permission denied
I have no name!@c25f16a4f1a6:/$
I have no name!@c25f16a4f1a6:/$ touch  /create_in_run/hoge
I have no name!@c25f16a4f1a6:/$
I have no name!@c25f16a4f1a6:/$ ls -l /create_in_run/hoge
-rw-r--r-- 1 501 dialout 0 Jan  4 09:20 /create_in_run/hoge
I have no name!@c25f16a4f1a6:/$
```