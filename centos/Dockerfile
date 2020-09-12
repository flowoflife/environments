# -*- coding: utf-8 -*-
FROM centos:7

ENV DEBIAN_FRONTEND noninteractive

RUN yum -y update
RUN yum -y install tar unzip curl vim cmake bzip2 readline-devel \
    zlib-devel bzip2-devel sqlite sqlite-devel openssl-devel \
    libXext.x86_64 libSM.x86_64 libXrender.x86_64 gcc gdbm-devel \
    gcc-c++ make libffi-devel python-devel git pciutils graphviz \
    kernel-devel kernel-headers patch libyaml-devel autoconf \
    automake wget libtool bison tk-devel opencv

# install java JRK v8
RUN yum -y install libXcomposite libXcursor libXi libXtst \
    libXrandr alsa-lib mesa-libEGL libXdamage mesa-libGL libXScrnSaver   
RUN yum -y install java-1.8.0-openjdk

# set Japanese support
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG="ja_JP.UTF-8"

# set Japan timezone
RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# install python3
RUN yum -y install python3

RUN echo export PATH=/root/.local/bin:$PATH >> ~/.bashrc
RUN source ~/.bashrc

# install requirements
ADD requirements.txt /root
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip --no-cache-dir install --upgrade --trusted-host pypi.python.org -r /root/requirements.txt
RUN rm -f /root/requirements.txt
RUN python3 -m pip install --upgrade tensorflow

RUN yum clean all

EXPOSE 8888 10000 54321

WORKDIR /home

CMD ["/bin/bash"]