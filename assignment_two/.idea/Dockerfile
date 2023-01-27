# syntax=docker/dockerfile:1


ARG PYTHON_VERSION

FROM ubuntu:18.04 AS base
WORKDIR /application
RUN apt-get update && apt-get install -y software-properties-common && apt-get install -y --no-install-recommends gcc 
RUN apt-get install -y wget build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev libffi-dev uuid-dev


FROM base AS python-3.8
RUN apt-get update && apt update && apt install software-properties-common -y \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get install -y python3.8 && cd /usr/local/bin && ln -sf python3.8 python3 \
    && apt-get install -y python3-pip \
    &&  rm -rf /var/lib/apt/lists/*
RUN pip3 install pytest nbmake pylint scipy wheel


FROM base AS python-3.9



FROM python-${PYTHON_VERSION} AS final