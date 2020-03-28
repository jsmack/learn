FROM ubuntu:latest
 
# update
RUN apt-get -y update && apt-get -y upgrade
 
# install basic packages
RUN apt-get install -y sudo wget bzip2
RUN apt-get install vim -y
 
###install anaconda3
WORKDIR /opt
# download anaconda package
# archive -> https://repo.continuum.io/archive/
RUN wget https://repo.continuum.io/archive/Anaconda3-2019.10-Linux-x86_64.sh
 
RUN /bin/bash /opt/Anaconda3-2019.10-Linux-x86_64.sh -b -p /opt/anaconda3
 
RUN rm -f Anaconda3-2019.10-Linux-x86_64.sh
ENV PATH /opt/anaconda3/bin:$PATH
 
# update pip and conda
RUN pip install --upgrade pip
 
RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev libglib2.0-0
RUN pip install opencv-python
WORKDIR /
RUN mkdir /work
 
# install jupyterlab
ENTRYPOINT ["jupyter", "lab","--no-browser", "--ip=0.0.0.0","--allow-root", "--LabApp.token=''"]
