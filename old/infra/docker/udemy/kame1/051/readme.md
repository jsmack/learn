# How to set ENV
- ENV is to be set environment variable
## What is the environment variables
- Environment variables are set to be shared by variables on tthe operating system.

## Example
```Dockerfile
ENV key1=value
ENV key2 value
ENV key3="v a l u e" key4=v\ a\ l\ u\ e
ENV key5 v a l u e
```

## Test
- Dockerfile
```Dockerfile
FROM ubuntu:latest

ENV key1=value
ENV key2 value
ENV key3="v a l u e" key4=v\ a\ l\ u\ e
ENV key5 v a l u e
```
- Build
```bash
>>> docker build .
Sending build context to Docker daemon  3.584kB
Step 1/5 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/5 : ENV key1=value
 ---> Running in 29b9273c3ca6
Removing intermediate container 29b9273c3ca6
 ---> 19ed131e8f80
Step 3/5 : ENV key2 value
 ---> Running in 7de48ee922f0
Removing intermediate container 7de48ee922f0
 ---> 944212e4781d
Step 4/5 : ENV key3="v a l u e" key4=v\ a\ l\ u\ e
 ---> Running in ffee8f4407c2
Removing intermediate container ffee8f4407c2
 ---> d9d220e3a798
Step 5/5 : ENV key5 v a l u e
 ---> Running in c96b3af5d02f
Removing intermediate container c96b3af5d02f
 ---> fd3e95581620
Successfully built fd3e95581620
>>>
```

- Run
```babsh
>>> docker run -it --rm fd3e95581620 bash
root@2ba88cc212e0:/# echo $key1
value
root@2ba88cc212e0:/# echo $key2
value
root@2ba88cc212e0:/# echo $key3
v a l u e
root@2ba88cc212e0:/# echo $key4
v a l u e
root@2ba88cc212e0:/# echo $key5
v a l u e
root@2ba88cc212e0:/#
root@2ba88cc212e0:/# env | grep key
key4=v a l u e
key5=v a l u e
key2=value
key3=v a l u e
key1=value
root@2ba88cc212e0:/#
```