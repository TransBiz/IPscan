# Created on Dec, 8, 2016
# @author: Yvictor

FROM yvictor/miniconda3
MAINTAINER yvictor

CD home/IPscan

RUN python pyipscan.py