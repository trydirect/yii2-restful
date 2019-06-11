FROM php:7.2-fpm

# Install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    mysql-client \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    locales \
    curl \
    supervisor \
    git \
    python-setuptools \
    python-pip \
    librabbitmq-dev \
    software-properties-common \
    && groupadd -r -g 2000 yii \
    && useradd -u 2000 -g 2000 -m -d /home/yii -s /bin/bash yii && adduser yii sudo \
    && echo "yii ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \
    && mkdir -p /etc/sudoers.d \
    && touch /etc/sudoers.d/privacy \
    && echo "Defaults        lecture = never" >> /etc/sudoers.d/privacy



