# -*- coding: utf-8 -*-
# Use an official ubuntu as a parent image
FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

# Install some TensorFlow dependencies, Python 3.5 and others
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-setuptools \
        python3-pip \
        python3-dev \
        build-essential \
        apt-utils \
        curl \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        rsync \
        software-properties-common \
        unzip \
        vim \
        cron \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

ENV DEBIAN_FRONTEND teletype

# Set the working directory
# /opt/project is used as default for docker container mapping in Pycharm
WORKDIR /home

# Copy the current directory contents into the container
ADD . /home

# or try this after copy app.tar into the same directory with Dockerfile
# ONBUILD ADD app.tar /opt/project

# Install any needed packages specified
RUN pip3 --no-cache-dir install --upgrade --trusted-host pypi.python.org -r /home/requirements.txt

# Make port available to the world outside this container
EXPOSE 6006 8888

# Run command when the container launches
CMD ["/bin/bash"]
