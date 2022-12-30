# Docker image 

- Docker image to tarball
  - `$ docker save <image> > <tarball>`
- Tarball to Docker image
  - `$ docker load < <tarball>`


- Return docker image from tarball

```bash
ubuntu@xxxxxxxxxxxx:~$ docker load < test_image.tar
777b2c648970: Loading layer [==================================================>]  5.848MB/5.848MB
abf174c5ac1e: Loading layer [==================================================>]  1.536kB/1.536kB
Loaded image ID: sha256:7c17fe44e0f2afc466c946734119bd8a9acc6401b18e0adb579d46bca888d09c
ubuntu@xxxxxxxxxxxx:~$ 
ubuntu@xxxxxxxxxxxx:~$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
<none>              <none>              7c17fe44e0f2        7 minutes ago       5.58MB
ubuntu@xxxxxxxxxxxx:~$ 
ubuntu@xxxxxxxxxxxx:~$ docker run -it 7c17fe44e0f2 sh
/ # ls -l
total 56
drwxr-xr-x    2 root     root          4096 Dec 16 10:31 bin
drwxr-xr-x    5 root     root           360 Jan  7 12:39 dev
drwxr-xr-x    1 root     root          4096 Jan  7 12:39 etc
-rw-r--r--    1 root     root             0 Jan  7 12:31 hoge
drwxr-xr-x    2 root     root          4096 Dec 16 10:31 home
drwxr-xr-x    7 root     root          4096 Dec 16 10:31 lib
drwxr-xr-x    5 root     root          4096 Dec 16 10:31 media
drwxr-xr-x    2 root     root          4096 Dec 16 10:31 mnt
drwxr-xr-x    2 root     root          4096 Dec 16 10:31 opt
dr-xr-xr-x  118 root     root             0 Jan  7 12:39 proc
drwx------    1 root     root          4096 Jan  7 12:39 root
drwxr-xr-x    2 root     root          4096 Dec 16 10:31 run
drwxr-xr-x    2 root     root          4096 Dec 16 10:31 sbin
drwxr-xr-x    2 root     root          4096 Dec 16 10:31 srv
dr-xr-xr-x   13 root     root             0 Jan  7 12:39 sys
drwxrwxrwt    2 root     root          4096 Dec 16 10:31 tmp
drwxr-xr-x    7 root     root          4096 Dec 16 10:31 usr
drwxr-xr-x   12 root     root          4096 Dec 16 10:31 var
/ # exit
ubuntu@xxxxxxxxxxxx:~$ 
```