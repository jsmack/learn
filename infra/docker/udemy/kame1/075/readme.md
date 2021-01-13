# Docker dameon configuration 
- data-root
  - /etc/docker/daemon.json
```json
{
    "data-root": "/new.docker/daeon/directory"
}
```


# Access permission check
```bash
ubuntu@ip-172-31-27-102:~/dsn_env_build$ cat /etc/passwd | tail -n2
aaaa:x:1111:1111:,,,:/home/aaaa:/bin/bash
bbbb:x:22221:22221:,,,:/home/bbbb:/bin/bash
ubuntu@ip-172-31-27-102:~/dsn_env_build$
ubuntu@ip-172-31-27-102:~/dsn_env_build$ docker run -u 1111 -v /home/aaaa:/home/aaaa -v /home/bbbb:/home/bbbb -it ubuntu bash
I have no name!@d357c8a74e01:/$
Try 'id --help' for more information.
I have no name!@d357c8a74e01:/$ id -u
1111
I have no name!@d357c8a74e01:/$ cd /home
I have no name!@d357c8a74e01:/home$ ls -l
total 8
drwxr-xr-x 2  1111  1111 4096 Jan  9 09:55 aaaa
drwxr-xr-x 2 22221 22221 4096 Jan  9 09:55 bbbb
I have no name!@d357c8a74e01:/home$ cd aaaa
I have no name!@d357c8a74e01:/home/aaaa$ touch hoge
I have no name!@d357c8a74e01:/home/aaaa$ ls -l
total 0
-rw-r--r-- 1 1111 root 0 Jan  9 09:58 hoge
I have no name!@d357c8a74e01:/home/aaaa$ cd ../bbbb
I have no name!@d357c8a74e01:/home/bbbb$ ls -l
total 0
I have no name!@d357c8a74e01:/home/bbbb$ touch hoge2
touch: cannot touch 'hoge2': Permission denied
I have no name!@d357c8a74e01:/home/bbbb$
```
