# How to control?
- It can be set in the Docker run option
  - `-v <host>:><container>`
- However, you can access it with root privileges

## TEST
### If the mount directory created
- Dockerfile
```Dockerfile
FROM ubuntu:latest
RUN mkdir new_dir
```

- build and build and run
```bash
>>> mkdir host_dir
>>>
>>> touch host_dir/file_at_host
>>>
>>> docker build .
Sending build context to Docker daemon  4.608kB
Step 1/2 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/2 : RUN mkdir /new_dir
 ---> Using cache
 ---> c5b7b9908b73
Successfully built c5b7b9908b73
>>>
>>> docker run -it --rm -v /xx/bb/cc/host_dir:/new_dir c5b7b9908b73 bash
root@815f3a1fcf18:/# ls -l /new_dir/
total 0
-rw-r--r-- 1 root root 0 Jan  4 06:45 file_at_host
root@69d89c0e7ef3:/# echo "hoge" > /new_dir/file_at_host
root@69d89c0e7ef3:/# exit
exit
>>> 
>>> cat host_dir/file_at_host
hoge
>>>
```

### If the mount directory not created
#### Auto create directory
- Dockerfile
```Dockerfile
FROM ubuntu:latest
```

- build and build and run
```bash
>>>
>>> docker build -f ./Dockerfile_no_dir .
Sending build context to Docker daemon  6.656kB
Step 1/1 : FROM ubuntu:latest
 ---> f643c72bc252
Successfully built f643c72bc252
>>>
>>> docker run -it --rm -v /xxx/bbb/ccc/host_dir:/new_dir_nyannya f643c72bc252 bash
root@96ec6f2a1673:/# ls -l /
total 48
lrwxrwxrwx   1 root root    7 Nov  6 01:21 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
drwxr-xr-x   5 root root  360 Jan  4 07:12 dev
drwxr-xr-x   1 root root 4096 Jan  4 07:12 etc
drwxr-xr-x   2 root root 4096 Apr 15  2020 home
lrwxrwxrwx   1 root root    7 Nov  6 01:21 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Nov  6 01:21 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Nov  6 01:21 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Nov  6 01:21 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Nov  6 01:21 media
drwxr-xr-x   2 root root 4096 Nov  6 01:21 mnt
drwxr-xr-x   3 root root   96 Jan  4 06:45 new_dir_nyannya
drwxr-xr-x   2 root root 4096 Nov  6 01:21 opt
dr-xr-xr-x 113 root root    0 Jan  4 07:12 proc
drwx------   2 root root 4096 Nov  6 01:25 root
drwxr-xr-x   1 root root 4096 Nov 25 22:25 run
lrwxrwxrwx   1 root root    8 Nov  6 01:21 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Nov  6 01:21 srv
dr-xr-xr-x  13 root root    0 Dec 31 08:36 sys
drwxrwxrwt   2 root root 4096 Nov  6 01:25 tmp
drwxr-xr-x   1 root root 4096 Nov  6 01:21 usr
drwxr-xr-x   1 root root 4096 Nov  6 01:25 var
root@96ec6f2a1673:/# ls -l /new_dir_nyannya/
total 4
-rw-r--r-- 1 root root 5 Jan  4 06:54 file_at_host
root@96ec6f2a1673:/# exit
exit
>>>
```