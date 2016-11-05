#!/usr/bin/env python
# encoding: utf-8
### Adapter

import time
import json
import configparser
#from bypy.bypy import ByPy
from .bypy import bypy
import by_adaptor
import os
import shutil

adaptor_config_path = 'config/config.ini'

def add_adaptor(adaptor_type = 'baiduyun', configdir = ''):
    if configdir == '':
        configdir = 'config/baiduyun' + str(int(time.time() * 1000))
    if adaptor_type == 'baiduyun':
        by_adaptor.add_adaptor(configdir)
    else :
        raise Exception('wrong adaptor_type: %s' % adaptor_type)
    config = configparser.ConfigParser()
    config.read(adaptor_config_path)
    if 'recloud' not in config:
        config['recloud'] = {}
    if 'adaptors' not in config['recloud']:
        config['recloud']['adaptors'] = '{}'
    adapter_list = json.loads(config['recloud']['adaptors'])
    adapter_list[configdir] = adaptor_type
    config['recloud']['adaptors'] = json.dumps(adapter_list)
    with open(adaptor_config_path, 'w') as configfile:
        config.write(configfile)


def del_adaptor(configdir):
    if os.path.exists(configdir):
        shutil.rmtree(configdir)
        config = configparser.ConfigParser()
        config.read(adaptor_config_path)
        if not 'recloud' in config:
            config['recloud'] = {}
        adaptor_list = json.loads(config['recloud']['adaptors'])
        adaptor_list.pop(configdir)
        config['recloud']['adaptors'] = json.dumps(adaptor_list)
        with open(adaptor_config_path, 'w') as configfile:
            config.write(configfile)


def get_all_adapters():
    config = configparser.ConfigParser()
    config.read(adaptor_config_path)
    if 'recloud' not in config:
        config['recloud'] = {}
    if 'adaptors' not in config['recloud']:
        config['recloud']['adaptors'] = '{}'

    adaptor_list = json.loads(config['recloud']['adaptors'])
    adaptors = []
    for configdir in adaptor_list:
        adaptors.append(Adaptor(configdir, adaptor_list[configdir]))
    return adaptors


class Adaptor(object):
    def __init__(self, configdir, adaptor_type = 'baiduyun'):
        '''
        :param configdir: 适配器配置文件目录
        :param adaptor_type: 适配器类型
        :return: 初始化一个适配器
        '''
        if not os.path.exists(configdir):
            raise Exception('configdir does not exist!!\n'
                            'Please add adaptor first!!')
        self._configdir = configdir;
        self.sub_adaptor = None
        if adaptor_type == 'baiduyun':
            self.sub_adaptor = ByPy(configdir=configdir)

    def info(self):
        '''
        :return: 返回容量信息
        Quota: 剩余容量
        Used: 已经使用容量
        '''
        return self.sub_adaptor.info()

    def upload(self, lpath='', rpath=''):
        '''
        :param lpath: 本地目录名
        :param rpath: 远程目录名
        :return:
        '''
        return self.sub_adaptor.upload(lpath, rpath)

    def download(self, remotefile, localpath=''):
        return self.sub_adaptor.download(remotefile,localpath)

    def delete(self, remotepath):
        return self.sub_adaptor.delete(remotepath)

    def list(self, remotepath = '',
		fmt = '$t $f $s $m $d',
		sort = 'name', order = 'asc'):
        '''
        :return: 文件列表
        '''
        return self.sub_adaptor.list(remotepath,fmt,sort,order)

    def destory(self):
        del_adaptor(self._configdir)


if __name__ == '__main__':
    '''
    Sample
    '''
    # 先创建一个适配器
    add_adaptor(adaptor_type='baiduyun')
    # 获取所有适配器
    adaptors = get_all_adapters();
    # 得到第一个适配器
    myad = adaptors[0]
    print(myad.info())
    # 查看根目录文件信息
    print(myad.list(remotepath=''))
    myad.upload('test.txt', 'test.txt')
    # 下载文件
    myad.download(remotefile='test.txt', localpath='test10.txt')
    # 删除文件
    myad.delete('test.txt')
    print(myad.list())
    # 删除这个适配器
    myad.destory()
    pass
