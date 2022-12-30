# How to tiny docker images
- Best practis
  - Minimize layers of Dokcer images
  - 
- Create layer instruction
  - RUN
  - COPY
  - ADD

# Exampe Ubunt package install
- apt-get or apt
  - apt update
    - Get new pakcage lists
  - apt-get install <package>
    - Package install

## Example Docker file
- Crete 5 layers
  - many layer and large...
```
FROM ubuntu:latest
RUN apt-get update
RUN apt-get install xxxx
RUN apt-get install yyyy
RUN apt-get install zzzz
RUN apt-get install wwww
```

- Crete 1 layer!
  - But it's hard to see
```
FROM ubuntu:latest
RUN apt-get update && apt-get install xxxx yyyy zzzz wwww
```

- So write it over multiple line with a backslash.
```
FROM ubuntu:latest
RUN apt-get update &&\
    apt-get install xxxx \
                    yyyy \
                    zzzz \
                    wwww
```