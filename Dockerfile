# Created on Dec, 8, 2016
# @author: Yvictor

FROM yvictor/docker_conda:cmpy
MAINTAINER yvictor

# install python3.5 and essential
# RUN apt-get update && apt-get install -y python3.5 python-dev wget cron build-essential
# install pip
# RUN wget https://bootstrap.pypa.io/get-pip.py -O- | python
# install python-lxml
# RUN apt-get update && apt-get install -y python-lxml


COPY . /IPscan
WORKDIR /IPscan

RUN python setup.py install
RUN python pyipscan.py
CMD python pyipscan.py
