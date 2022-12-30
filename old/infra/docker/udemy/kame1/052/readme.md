# WORKDIR instruction
- WORKDIR changes the current directory when executing other instruction
- If the directory specified by WORKDIR does not exist it will be created.

## Format
```Dockerfile
WORKDIR <absolute path>
```

## Where is running instrucion
- RUN or other instruction are executing in the  /(root) directory

### Example
#### sample_file is not created in /sample_dir
```Dockerfile
FROM ubuntu:latest

RUN mkdir sample_dir    # <- Create a directory in the / directory
RUN cd sample_dir       # <- change directory, However, it is valid only for the RUN instruction
RUN touch sample_file   # <- Create a file in the / directory
```

- build & run
```bash
>>> docker build .
Sending build context to Docker daemon  3.584kB
Step 1/5 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/5 : FROM ubuntu:latest
 ---> f643c72bc252
Step 3/5 : RUN mkdir sample_dir    # <- Create a directory in the / directory
 ---> Running in dcdc594e279a
Removing intermediate container dcdc594e279a
 ---> 3e4646eb6a39
Step 4/5 : RUN cd sample_dir       # <- change directory, However, it is valid only for the RUN instruction
 ---> Running in 7a1edbfd4c62
Removing intermediate container 7a1edbfd4c62
 ---> b05f4ea58b7b
Step 5/5 : RUN touch sample_file   # <- Create a file in the / directory
 ---> Running in f804916226b1
Removing intermediate container f804916226b1
 ---> fabc873cbfb7
Successfully built fabc873cbfb7
>>>
>>> docker run -it --rm fabc873cbfb7 bash
root@3b7811fd62c7:/# ls -l /sample_*
-rw-r--r-- 1 root root    0 Jan  1 07:48 /sample_file

/sample_dir:
total 0
root@3b7811fd62c7:/#
```

#### sample_file is created in /sample_dir
- Dockerfile_create
```Dockerfile
FROM ubuntu:latest

RUN mkdir sample_dir \
&&  cd sample_dir \
&&  touch sample_file
```
- build & run
```bash
>>> docker build -f ./Dockerfile_create .
Sending build context to Docker daemon  6.144kB
Step 1/2 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/2 : RUN mkdir sample_dir &&  cd sample_dir &&  touch sample_file
 ---> Running in 1ae323c8db8a
Removing intermediate container 1ae323c8db8a
 ---> f6eaa6a53bf4
Successfully built f6eaa6a53bf4
>>> docker run -it --rm f6eaa6a53bf4 bash
root@6b5e802c9390:/#
root@6b5e802c9390:/# ls -l /sample_dir/*
-rw-r--r-- 1 root root 0 Jan  1 07:56 /sample_dir/sample_file
root@6b5e802c9390:/#
```

#### Use WORKDIR instruction
- Dockerfile_WORKDIR
```Dockerfile
FROM ubuntu:latest

RUN mkdir sample_dir
WORKDIR /sample_dir
RUN touch sample_file
```
- build & run
```bash
>>> docker build -f ./Dockerfile_WORKDIR .
Sending build context to Docker daemon   7.68kB
Step 1/5 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/5 : FROM ubuntu:latest
 ---> f643c72bc252
Step 3/5 : RUN mkdir sample_dir
 ---> Running in e7b33495ffcd
Removing intermediate container e7b33495ffcd
 ---> 119b50f11e2f
Step 4/5 : WORKDIR /sample_dir
 ---> Running in d4d6c4bd4498
Removing intermediate container d4d6c4bd4498
 ---> d3417c95b927
Step 5/5 : RUN touch sample_file
 ---> Running in ba73eec035e3
Removing intermediate container ba73eec035e3
 ---> 5d4f587dce4e
Successfully built 5d4f587dce4e
>>> docker run -it --rm 5d4f587dce4e bash
root@6acbb2ea37ee:/sample_dir# 
root@6acbb2ea37ee:/sample_dir# ls -l /sample_dir/*
-rw-r--r-- 1 root root 0 Jan  1 08:00 /sample_dir/sample_file
root@6acbb2ea37ee:/sample_dir#
```

#### Use WORKDIR instruction and not use mkdir 
- Dockerfile_WORKDIR_not_mkdir
```Dockerfile
FROM ubuntu:latest

WORKDIR /sample_dir
RUN touch sample_file
```
- build & run
```bash
>>> docker build -f ./Dockerfile_WORKDIR_not_mkdir .
Sending build context to Docker daemon  9.728kB
Step 1/3 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/3 : WORKDIR /sample_dir
 ---> Running in fb7f01e6ba3b
Removing intermediate container fb7f01e6ba3b
 ---> 2475b4e23d61
Step 3/3 : RUN touch sample_file
 ---> Running in 5dbd8c636452
Removing intermediate container 5dbd8c636452
 ---> e240628e3d32
Successfully built e240628e3d32
>>>
>>> docker run -it --rm e240628e3d32 ls -l /sample_dir/sample_file
-rw-r--r-- 1 root root 0 Jan  1 08:05 /sample_dir/sample_file
>>>
```