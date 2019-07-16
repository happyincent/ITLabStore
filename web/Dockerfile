FROM python:3-alpine
MAINTAINER ddl <itlab.ee.ncku.edu.tw>

# Environment
ENV PYTHONUNBUFFERED 1
ARG TZ=Asia/Taipei

RUN mkdir -p mkdir /www
WORKDIR /www

### Django
COPY ./app/requirements.txt /www/requirements.txt

RUN set -e; \
    apk update \
    && apk add --virtual .build-deps build-base python3-dev linux-headers \
    && pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r /www/requirements.txt \
    && apk del .build-deps

# Setup timezone
RUN apk add --update --no-cache tzdata && \
    cp /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    date && \
    apk del tzdata

# Cleanup
RUN rm -rf /var/cache/* /tmp/*
