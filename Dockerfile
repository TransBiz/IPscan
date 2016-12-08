# Created on Dec, 8, 2016
# @author: Yvictor

FROM yvictor/miniconda3
MAINTAINER yvictor

COPY . /IPscan
WORKDIR /IPscan

ENV PATH=root/miniconda3/bin

CMD ["python", "pyipscan.py"]