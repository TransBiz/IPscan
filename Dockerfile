# Created on Dec, 8, 2016
# @author: Yvictor

FROM samsam2310/python-crawler-base
MAINTAINER yvictor


COPY . /IPscan
WORKDIR /IPscan

RUN python setup.py install

RUN python pyipscan.py