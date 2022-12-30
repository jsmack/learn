# Container file system
- Create container1 ( efaac7ddb8ce )
```
$ docker run -it ubuntu bash
root@efaac7ddb8ce:/# touch test1
root@efaac7ddb8ce:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  test1  tmp  usr  var
root@efaac7ddb8ce:/# 
```
- Create container2 ( 428e60bc01f5 )
  - Not found touch1 file
```
$ docker run -it ubuntu bash
root@428e60bc01f5:/# touch test2
root@428e60bc01f5:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  test2  tmp  usr  var
root@428e60bc01f5:/# 
```

- Changing the file in container 1 does not change the file in container 2