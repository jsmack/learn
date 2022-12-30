# What's "-it" option
- i(stdin)
  - Input is possible
- t
  - The display becomes beautiful
  - enable bash-completion

- only t option
  - wait .... ( not exit...)
```
$ docker run -t ubuntu bash
root@9ed42d4638aa:/# ls

```

- flow(chanel)
  - stdin(keyboard) -> program -> stdout or stdeer -> display

- only i option
  - not pretty
```
$ docker run -i ubuntu bash

ls
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
exit
```
