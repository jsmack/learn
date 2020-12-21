# Command override

- ubuntu image default command is bash

- test
```
$ docker run ubuntu bash
$
```

- docker run add option -it
```
$ docker run -it ubuntu 
root@482876b24729:/# 
root@482876b24729:/# 
root@482876b24729:/# ps
  PID TTY          TIME CMD
    1 pts/0    00:00:00 bash
   10 pts/0    00:00:00 ps
root@482876b24729:/# 
```

- Override bash command with ls command
```
$ docker run ubuntu ls
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
$ 
```