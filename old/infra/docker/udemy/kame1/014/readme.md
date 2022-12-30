
- container restart

```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
f7de31cb8fcd        ubuntu              "bash"              13 seconds ago      Exited (0) 10 seconds ago                       nice_curran
$
$
$docker restart stupefied_margulis
nice_curran
$
$docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
88e62b113daa        ubuntu              "bash"              35 seconds ago      Up 3 seconds                            stupefied_margulis
$
```

- connect container
```
$ docker exec -it stupefied_margulis bash
root@88e62b113daa:/# 
root@88e62b113daa:/# 
root@88e62b113daa:/# pgrep bash
1
17
root@88e62b113daa:/# exit
```

- What is the difference between exit and detach
  - exit
    - process exit and logout 
  - detach
    - not exit process and logout

- detach
  - ctrl+p+q

- attach
```
$ docker attach stupefied_margulis 
root@88e62b113daa:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  test  tmp  usr  var
root@88e62b113daa:/# pgrep bash
1
root@88e62b113daa:/# 
```