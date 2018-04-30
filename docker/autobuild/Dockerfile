FROM docker/whalesay

RUN apt-get -y update && apt-get install cowsay fortunes -y && apt-get clean all

CMD /usr/games/fortune | cowsay 
