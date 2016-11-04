#!/usr/bin/env python
#encoding:utf-8
### 百度云adaptor
import os
from bypy.bypy import ByPy

def add_adaptor(configdir):
    if os.path.exists(configdir):
        raise Exception("configdir existed!")
    os.makedirs(configdir)
    by = ByPy(configdir=configdir)
    # print(by.info())


if __name__ == '__main__':
    add_adaptor('test')
