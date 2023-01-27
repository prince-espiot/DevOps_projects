# syntax=docker/dockerfile:1

ARG PYTHON_VERSION

FROM ubuntu:18.04 AS base
WORKDIR /application
RUN apt-get update && apt-get install -y software-properties-common && apt-get install -y --no-install-recommends gcc wget build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev libffi-dev uuid-dev

FROM base AS python-version-3.8

RUN wget https://www.python.org/ftp/python/3.8.14/Python-3.8.14.tgz && tar xzf Python-3.8.14.tgz && rm -f *.tgz && cd Python-3.8.14 && ./configure && make altinstall && cd /application && rm -r Python-3.8.14/  && cd /usr/local/bin && ln -sf python3.8 python3 && python3 -m pip install --upgrade pip && apt purge -y python2.7-minimal &&  apt-get -y purge python3.6 && apt-get -y autoremove && apt-get clean &&  rm -rf /var/lib/apt/lists/* && pip3 install pytest nbmake pylint wheel

FROM base AS python-version-3.9

RUN wget https://www.python.org/ftp/python/3.9.14/Python-3.9.14.tgz && tar xzf Python-3.9.14.tgz && rm -f *.tgz && cd Python-3.9.14 && ./configure && make altinstall && cd /application && rm -r Python-3.9.14/ && cd /usr/local/bin && ln -sf python3.9 python3 && python3 -m pip install --upgrade pip && apt purge -y python2.7-minimal &&  apt-get -y purge python3.6 && apt-get -y autoremove && apt-get clean &&  rm -rf /var/lib/apt/lists/* && pip3 install pytest nbmake pylint wheel

FROM python-version-${PYTHON_VERSION} AS final


