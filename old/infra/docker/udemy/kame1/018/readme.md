# Push created imange from local to docker hub
- push 
  - Mounted from?
    - already on the docker hub docker image layer
    - use library/ubuntu image layer
```
$ docker push xxxx/docker-lean
Using default tag: latest
The push refers to repository [docker.io/xxxx/docker-lean]
b34a6099704f: Pushed 
f6253634dc78: Mounted from library/ubuntu 
9069f84dbbe9: Mounted from library/ubuntu 
bacd3af13903: Mounted from library/ubuntu 
latest: digest: sha256:1f55f04dfc0fef840f45a9c45cdfb54386da2ed33701301c7f4fde6c3fe94f86 size: 1150
$ 
```
