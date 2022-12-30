# Summary

- what is Docker file?
  - Docker file is blueprint of docker image.
  - Docker file is text file
  - Write instruction in Docker file
  
- How to write a Docker file
  - List FROM at the beginning
    - Write the base Docker image in FROM
    - Write the command in RUN

- How to build
  - Navigate to the location of you Docker file
  - Execute command
    - docker build .
      - . is current directory
    - docker build -t <name> <directory>

- Docker images are usually generated from docker file.
