FROM python:3-alpine
MAINTAINER ddl <itlab.ee.ncku.edu.tw>

# Environment
ENV TZ=Asia/Taipei
RUN apk update && \
    apk add --no-cache nano curl

### Copy files
COPY updateDB.sh /etc/periodic/15min/updateDB
COPY clearLog.sh /etc/periodic/daily/clearLog
COPY run.sh /run.sh
RUN chmod +x \
        /run.sh \
        /etc/periodic/15min/updateDB \
        /etc/periodic/daily/clearLog

### Django
ENV PYTHONUNBUFFERED 1
WORKDIR /www
COPY ./django /www/
RUN apk add --no-cache \
        python3-dev build-base linux-headers pcre-dev \
        && \
    pip install -r requirements.txt

### Timezone
RUN apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone
