FROM picorb/python

RUN apt-add-repository "deb http://cran.cnr.berkeley.edu/bin/linux/ubuntu trusty/" && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9

RUN apt-get update --fix-missing

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y supervisor libpq-dev npm
RUN mkdir -p /var/log/supervisor && ln -s /usr/bin/nodejs /usr/bin/node

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN apt-get autoremove -y

RUN npm install -g bower coffee-script stylus cssmin
RUN npm install jeet

WORKDIR /app
ADD requirements.txt /app/
RUN virtualenv /env --system-site-packages
RUN /env/bin/pip install -r requirements.txt
RUN pip install supervisor-stdout
ADD . /app
RUN /env/bin/python manage.py collectstatic --noinput
ADD ./config/supervisord.conf /etc/supervisor/conf.d/supervisord-django.conf

VOLUME ["/sockets"]

EXPOSE 8080 4000 5000
CMD ["/usr/bin/supervisord", "-n"]
#ENTRYPOINT ["/env/bin/python", "manage.py"]
