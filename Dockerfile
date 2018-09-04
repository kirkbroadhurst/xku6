FROM nginx
COPY root /usr/share/nginx/html/
RUN rm /etc/nginx/conf.d/default.conf
#COPY xku6.conf /etc/nginx/conf.d
COPY nginx.conf /etc/nginx

