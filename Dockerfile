# Created on Dec, 8, 2016
# @author: Yvictor

FROM yvictor/ipscan
MAINTAINER yvictor

CD home/IPscan

RUN python pyipscan.py