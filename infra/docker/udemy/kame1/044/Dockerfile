FROM ubuntu:latest

RUN apt-get update &&  \
    apt-get install -y \
    curl \
    cvs  \
    nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["pwd"]
