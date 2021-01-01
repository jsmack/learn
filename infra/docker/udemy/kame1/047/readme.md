# COPY instruction
- You can import the files int the build context into the docker image by using COPY instruction. 


## Check
- Create tempfile
```bash
$ dd if=/dev/zero of=./tempfile bs=1024 count=1000
1000+0 records in
1000+0 records out
1024000 bytes transferred in 0.012074 secs (84810381 bytes/sec)
$
$  ls -lh
total 2016
-rw-r--r--  1 kim  staff    44B 12 31 14:16 Dockerfile
-rw-r--r--  1 kim  staff   1.0M 12 31 14:16 tempfile
$
```

- Dockerfile
```Dockerfile
FROM ubuntu:latest
RUN mkdir /new_dir
COPY tempfile /new_dir

CMD ["/bin/bash"]
```

- build
```docker
$ docker build .
Sending build context to Docker daemon  1.029MB
Step 1/4 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/4 : RUN mkdir /new_dir
 ---> Using cache
 ---> 6e452d4b7a0b
Step 3/4 : COPY tempfile /new_dir
 ---> b68a83858dd4
Step 4/4 : CMD ["/bin/bash"]
 ---> Running in 3584a378cd21
Removing intermediate container 3584a378cd21
 ---> 1ec45db68dab
Successfully built 1ec45db68dab
$
```

- Check file
```bash
$ docker run -it 1ec45db68dab bash
root@d72b93013220:/# ls -l /new_dir/
total 1000
-rw-r--r-- 1 root root 1024000 Dec 31 05:16 tempfile
root@d72b93013220:/#
```