#FROM ubuntu:latest
## CUDAToolkit image
FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04


RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim

WORKDIR /opt

RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh && \
    sh Anaconda3-2020.11-Linux-x86_64.sh -b -p /opt/anaconda3 && \
    rm -f /opt/Anaconda3-2020.11-Linux-x86_64.sh

ENV PATH /opt/anaconda3/bin:$PATH

RUN pip install --upgrade pip && pip install \
  keras==2.4.3 \
  scipy==1.4.1 \
  tensorflow-gpu==2.4.0

WORKDIR /

CMD [ "jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''" ]
