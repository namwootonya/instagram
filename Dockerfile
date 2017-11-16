FROM        namwootonya/base
MAINTAINER  garson1362@gmail.com

ENV         LANG C.UTF-8

COPY        . /srv/app
RUN         /root/.pyenv/versions/app/bin/pip install -r \
            /srv/app/requirements.txt

WORKDIR     /srv/app
RUN         pyenv local app

RUN         cp /srv/app/.config/nginx/nginx.conf \
                /etc/nginx/nginx.conf
RUN         cp /srv/app/.config/nginx/app.conf \
                /etc/nginx/sites-available/
RUN         rm -rf /etc/nginx/sites-enabled/*
RUN         ln -sf /etc/nginx/sites-available/app.conf \
                    /etc/nginx/sites-enabled/app.conf

RUN         mkdir -p /var/log/uwsgi/app

WORKDIR     /srv/app/instagram
RUN         /root/.pyenv/versions/app/bin/python manage.py collectstatic --noinput
RUN         /root/.pyenv/versions/app/bin/python manage.py migrate --noinput

RUN         cp /srv/app/.config/supervisor/* \
                /etc/supervisor/conf.d/
CMD         supervisord -n

EXPOSE      80
