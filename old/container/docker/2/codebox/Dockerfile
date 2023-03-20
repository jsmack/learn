FROM javierprovecho/docker-codebox

MAINTAINER james
# get node exporter

RUN mkdir -p /var/tmp
WORKDIR /var/tmp
RUN  curl --proxy xxx.xx.xxx:8080 -L https://github.com/prometheus/node_exporter/releases/download/v0.16.0-rc.1/node_exporter-0.16.0-rc.1.linux-amd64.tar.gz -o node_exporter-0.16.0-rc.1.linux-amd64.tar.gz \
     tar xzf node_exporter-0.16.0-rc.1.linux-amd64.tar.gz 

WORKDIR /var/tmp/node_exporter-0.16.0-rc.1.linux-amd64
