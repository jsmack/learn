# Create a docker environment on AWS
- Create ec2 instance
- Stop instance
- Start instance
- Chagen permission
  - 644 to 400
```bash
>>> chmod 400 xxxx.pem
>>> ls -l xxxx.pem
-r--------@ 1 www  staff  1700  1  7 21:08 xxxx.pem
>>> 
```
- Connect from host to aws ec2 instance
```bash
 >>> ssh -i xxxx.pem ubuntu@xxxx.compute.amazonaws.com

Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-1029-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Jan  7 12:15:49 UTC 2021

  System load:  0.01              Processes:             102
  Usage of /:   16.8% of 7.69GB   Users logged in:       0
  Memory usage: 18%               IPv4 address for eth0: 172.31.27.102
  Swap usage:   0%

1 update can be installed immediately.
0 of these updates are security updates.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@xxxxxxxxxxxx:~$
```

- Update packages
```bash
ubuntu@xxxxxxxxxxxx:~$ sudo apt-get update
ubuntu@xxxxxxxxxxxx:~$ 
ubuntu@xxxxxxxxxxxx:~$ sudo apt-get install docker.io
ubuntu@xxxxxxxxxxxx:~$ docker --version
Docker version 19.03.8, build afacb8b7f0
ubuntu@xxxxxxxxxxxx:~$ 
```

- Check docker images
  - By the default you do not have permission to run docker commands
```bash
>>> docker images
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.40/images/json: dial unix /var/run/ubuntu@xxxxxxxxxxxx:~$  
ubuntu@xxxxxxxxxxxx:~$  docker.sock: connect: permission denied
ubuntu@xxxxxxxxxxxx:~$  dsudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu@xxxxxxxxxxxx:~$ 

```

- Make docker group
```bash
ubuntu@xxxxxxxxxxxx:~$  sudo gpasswd -a ubuntu docker
Adding user ubuntu to group docker
ubuntu@xxxxxxxxxxxx:~$ 
```

- Check if docker command can be executed by ubuntu user
```bash
ubuntu@xxxxxxxxxxxx:~$  exit
 >>> ssh -i xxxx.pem ubuntu@xxxx.compute.amazonaws.com
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-1029-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Jan  7 12:22:14 UTC 2021

  System load:  0.03              Processes:                105
  Usage of /:   23.8% of 7.69GB   Users logged in:          0
  Memory usage: 27%               IPv4 address for docker0: 172.17.0.1
  Swap usage:   0%                IPv4 address for eth0:    172.31.27.102


80 updates can be installed immediately.
38 of these updates are security updates.
To see these additional updates run: apt list --upgradable


Last login: Thu Jan  7 12:15:51 2021 from 126.74.183.8
ubuntu@xxxxxxxxxxxx:~$  docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu@xxxxxxxxxxxx:~$  exit
```

- Create a suitable docker image
```bash
>>> mkdir context_build
>>> cd context_build
>>> docker build .
Sending build context to Docker daemon  2.048kB
Step 1/2 : FROM alpine:latest
latest: Pulling from library/alpine
801bfaa63ef2: Pull complete
Digest: sha256:3c7497bf0c7af93428242d6176e8f7905f2201d8fc5861f45be7a346b5f23436
Status: Downloaded newer image for alpine:latest
 ---> 389fef711851
Step 2/2 : RUN touch hoge
 ---> Running in 5ce54e52a3d0
Removing intermediate container 5ce54e52a3d0
 ---> 7c17fe44e0f2
Successfully built 7c17fe44e0f2
>>>
>>> docker save 7c17fe44e0f2 > test_image.tar
>>> ls -l
total 11456
-rw-r--r--  1 www  staff       34  1  7 21:32 Dockerfile
-rw-r--r--  1 www  staff  5860864  1  7 21:32 test_image.tar
>>> ls -lh
total 11456
-rw-r--r--  1 www  staff    34B  1  7 21:32 Dockerfile
-rw-r--r--  1 www  staff   5.6M  1  7 21:32 test_image.tar
>>>
```

- Send docker image tar from host to aws ec2
```bash
>>>
>>> sftp -i ~/Downloads/20210107_mydocker.pem ubuntu@xxxx.compute.amazonaws.com
Connected to xxxx.compute.amazonaws.com.
sftp>
sftp> put test_image.tar ./
Uploading test_image.tar to /home/ubuntu/./test_image.tar
test_image.tar                                                                                                                                                                                                    100% 5724KB   1.3MB/s   00:04
sftp> lpwd
Local working directory: /Users/www/work/git/learn/infra/docker/udemy/kame1/069/context_build
sftp> ls
test_image.tar
sftp>
```