# What if the Dockerfile does not exist in the build context?
- Error!
```
>>> docker build .
unable to prepare context: unable to evaluate symlinks in Dockerfile path: lstat /_xx/xx/xx/xx/Dockerfile: no such file or directory
>>>
```

- Is it possible to specify a Dockerfile
```
>>> docker build -f <docerfilename> <build contrext>
```

## What do you use it?
### For example,
- The depending on the environment, Dockerfile may be returned
  - Dockerfile.dev
  - Dockerfile.test


## TEST
```bash
>>> find ./
./
.//Dockerfile.dev
.//test_dir
>>>
>>> cd test_dir
>>>
>>>  docker build -f ../Dockerfile.dev .
Sending build context to Docker daemon  1.583kB
Step 1/3 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/3 : RUN mkdir /new_dir
 ---> Using cache
 ---> 6e452d4b7a0b
Step 3/3 : CMD ["/bin/bash"]
 ---> Running in ec1567c4d391
Removing intermediate container ec1567c4d391
 ---> e614885f97b6
Successfully built e614885f97b6
>>>
```
