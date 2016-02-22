FROM phusion/passenger-full:0.9.18

# Set correct environment variables
ENV HOME /root

# Use bageimage-docker's init process
CMD ["/sbin/my_init"]

# Enable Nginx and Passenger
RUN rm -f /etc/service/nginx/down

RUN rm /etc/nginx/sites-enabled/default
ADD webapp.conf /etc/nginx/sites-enabled/webapp.conf
RUN mkdir /home/app/webapp
COPY www /home/app/webapp/public/

# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 80
