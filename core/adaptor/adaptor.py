#!/usr/bin/env python
# encoding: utf-8
### Adapter

from bypy.bypy import ByPy
import by_adaptor
import os
def add_adaptor(configdir, adaptor_type = 'baiduyun'):
    if adaptor_type == 'baiduyun':
        by_adaptor.add_adaptor(configdir)


def del_adaptor(configdir):
    if os.path.exists(configdir):
        os.removedirs(configdir)


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

if __name__ == '__main__':
    '''
    Sample
    '''
    # 先创建一个适配器
    add_adaptor(configdir='test1',adaptor_type='baiduyun')
    # 用配置目录名初始化一个适配器实例
    myad = Adaptor('test1')
    # 获得适配器容量信息
    print(myad.info())
    # 查看根目录文件信息
    print(myad.list(remotepath=''))
    #myad.upload('test.txt', 'test.txt')
    # 下载文件
    myad.download(remotefile='test.txt', localpath='test10.txt')
    # 删除文件
    myad.delete('test.txt')
    print(myad.list())
    pass