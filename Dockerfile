# Created on Dec, 8, 2016
# @author: Yvictor

FROM yvictor/miniconda3
MAINTAINER yvictor

CMD git clone https://github.com/Yvictor/IPscan.git
CMD cd home/IPscan

RUN python pyipscan.py