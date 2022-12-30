# Instruction
## RUN
- RUN executes linux command.

- example
```
# FROM is base image
FROM ubuntu:latest

# Execute command(instruction)
RUN touch test
RUN echo 'hello world' >> test
```

- build
  - A layser is created for each RUN command

```
docker build .
Sending build context to Docker daemon  3.584kB
Step 1/3 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/3 : RUN touch test
 ---> Using cache
 ---> aaf7263913df                              <-  touch command layer
Step 3/3 : RUN echo 'hello world' >> test
 ---> Running in 0b075e2e1a5d                   <-  echo command  layer
Removing intermediate container 0b075e2e1a5d
 ---> 8e72883fc3ba
Successfully built 8e72883fc3ba
```

- check
```
>>> docker run -it 8e72883fc3ba bash
root@fe0428596d13:/# cat test
hello world
root@fe0428596d13:/# exit
exit
>>>
```
