FROM nginx

MAINTAINER john
ARG host

# copy configuration file
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
RUN sed -e  "s!__LOG_DIR__!/logs/${host}/nginx!g" /etc/nginx/nginx.conf  > /etc/nginx/nginx.conf.new
RUN mv /etc/nginx/nginx.conf.new /etc/nginx/nginx.conf

CMD /usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf
