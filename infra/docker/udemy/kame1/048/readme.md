# What is difference between ADD and COPY
- COPY
  - If you just want to copy files and folders, use COPY
  - If you want to decompress file and copy, use ADD
    - The ADD instruction is automatically decompressed
  
## Test
```bash
mkdir sample_dir
>>> echo 'hoge' >> ./sample_dir/hoge
>>>
>>> tar cf ./sample_dir.tar ./sample_dir
>>>
>>> tar tvf ./sample_dir.tar
drwxr-xr-x  0 kim    staff       0 12 31 15:56 ./sample_dir/
-rw-r--r--  0 kim    staff       5 12 31 15:56 ./sample_dir/hoge
>>>
>>> rm -rf ./sample_dir
>>> tar tvf sample_dir.tar
drwxr-xr-x  0 kim    staff       0 12 31 15:56 ./sample_dir/
-rw-r--r--  0 kim    staff       5 12 31 15:56 ./sample_dir/hoge
>>> rm -rf ./sample_dir.tar
>>>
>>> cat Dockerfile
FROM ubuntu:latest
RUN mkdir /new_dir
COPY sample_dir.tar /new_dir

CMD ["/bin/bash"]
>>>
```
```bash
>>> docker build .
Sending build context to Docker daemon  6.144kB
Step 1/4 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/4 : RUN mkdir /new_dir
 ---> Using cache
 ---> 6e452d4b7a0b
Step 3/4 : ADD sample_dir.tar /new_dir
 ---> d545c7ed5efd
Step 4/4 : CMD ["/bin/bash"]
 ---> Running in 67c50a7e43b2
Removing intermediate container 67c50a7e43b2
 ---> 9df6de737692
Successfully built 9df6de737692
>>>
```
```bash
>>> docker run -it 9df6de737692 bash
root@175ff171d6e2:/# ls -lR /new_dir/
/new_dir/:
total 4
drwxr-xr-x 2 501 dialout 4096 Dec 31 06:56 sample_dir

/new_dir/sample_dir:
total 4
-rw-r--r-- 1 501 dialout 5 Dec 31 06:56 hoge
root@175ff171d6e2:/#
root@175ff171d6e2:/# cat /new_dir/sample_dir/hoge
hoge
root@175ff171d6e2:/#
```
