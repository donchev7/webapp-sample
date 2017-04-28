FROM python:3.5-alpine
MAINTAINER B.Blagovest Donchev <contact@donchev.is>

RUN apk update && addgroup www-user && adduser -s /bin/bash -D -G www-user www-user \
 && rm -rf /var/cache/apk/*

ENV INSTALL_PATH /webapp-sample
WORKDIR $INSTALL_PATH

COPY . .
RUN pip install --upgrade pip \
	&& pip install -r requirements.txt


RUN chown -R www-user:www-user $INSTALL_PATH
EXPOSE 8000

USER www-user
CMD gunicorn -c file:config/gunicorn.py "webapp-sample.app:create_app()"

