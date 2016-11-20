# -* - coding: UTF-8 -* -
from configparser import ConfigParser
from adaptor.adaptor import *

class SyncException(Exception):
    def __init__(self):
        super().__init__('Sync failed')

def get_config():
    cfg = ConfigParser()
    if os.path.exists('.recloud.cfg'):
        return cfg.read('.recloud.cfg')
    else:
        return None
def save_config(cfg):
    cfg.write(open('.recloud.cfg', 'w'))
# 如果同步打开，检查本地配置与云配置的差异，并同步（更新）
def sync_to_cloud():
    raise SyncException
# 如果加密打开，尝试对云端的配置进行解密
def sync_from_cloud():
    return SyncException
# 如果存在多个设备时，尝试更新所有云节点的配置
def sync_between_devices():
    cfg = get_config()
    # 如果加密关闭
    if cfg.get('overview', 'encrypt') == 'off':
        return SyncException
    # 如果加密打开
    else:
        return SyncException
# 以下方法由recloud调用
def update_when_node_deleted(self, node_seq):
    # 当节点被删除时
    cfg = get_config()
    deleted_adaptor = get_all_adapters()[node_seq]
    info = deleted_adaptor.info()
    # 删除本地对应节点配置
    try:
        cfg.remove_section('node_'+node_seq)
        deleted_adaptor.destory()
    except ConfigParser.NoSectionError as e:
        print(e)
    total_quota = cfg.getint('overview', 'total_quota')
    available_quota = cfg.getint('overview', 'available_quota')
    cfg.set('overview', 'total_quota', total_quota-info['Quota'])
    cfg.set('overview', 'available_quota', total_quota-info['Used'])
    cfg.set('overview', 'last_modified', time.time())
    # 更新overview，打上最新的时间戳
    # 如果开启了配置云同步选项，向云端发起同步请求
    if cfg.get('overview', 'sync') == 'on':
        try:
            sync_to_cloud()
        except SyncException as e:
            print(e)

def update_when_node_added(self, node_seq, adaptor):
    # 当新增一个节点时
    info = adaptor.info()
    cfg = get_config()
    node_name = 'node_' + node_seq
    # 在本地增加对应节点配置
    cfg.add_section(node_name)
    cfg.set(node_name, 'type', info['type'])
    cfg.set(node_name, 'total_quota', info['Quota'])
    cfg.set(node_name, 'available_quota', info['Used'])
    # 更新overview，打上最新的时间戳
    total_quota = cfg.getint('overview', 'total_quota')
    available_quota = cfg.getint('overview', 'available_quota')
    cfg.set('overview', 'total_quota', total_quota+info['Quota'])
    cfg.set('overview', 'available_quota', total_quota+info['Used'])
    import time
    cfg.set('basic', 'last_modified', time.time())
    # 如果开启了配置云同步选项，向云端发起同步请求
    if cfg.get('overview', 'sync') == 'on':
        # 调用sys_upload
        # 若同步成功
        try:
            sync_from_cloud()
            sync_between_devices()
        # 若同步失败
        except SyncException as e1:
            try:
                sync_to_cloud()
            except SyncException as e2:
                print('Is your internet ok?')
    # 新建一个以设备名目录，将本地配置加密分块后上传至该目录
    # 同步时若发现sys目录下已经有一个或多个设备名目录，下面有一个recloud_config_<[0-9]+>的文件包
    #   下载到config_cache目录下的上一个设备名目录尝试解锁
    #       若解锁失败，保留日志
    #       若解锁成功，恢复并更新本地配置


def self_check():
    all_adaptor = get_all_adapters()
    # 检查cfg文件是不是被非法篡改，用于doctor
    # 检查overview和node的不同步
        # 是否有node增加或删除而overview未更新的情况
    # 检查配置和adaptor的不同步
        # 配置里是不是有不存在的adaptor
# 第一次运行时的初始化
def initialize():
    import os
    if get_config() == None:
        # 新建本地配置
        cfg = ConfigParser()
        cfg.add_section('basic')
        cfg.add_section('overview')
        # 获取本机名称
        import platform
        device_name = platform.node()
        cfg.set('basic', 'device', device_name)
        device_info = platform.platform()
        cfg.set('basic', 'system', device_info)
        # 默认打开同步设置
        cfg.set('basic', 'sync', 'on')
        # 默认关闭加密设置
        cfg.set('basic', 'encrypt', 'off')
        # 默认关闭垃圾箱
        cfg.set('basic', 'trash_bin', 'off')
        # 设置用户名
        user_name = input("What's your name?\n")
        conf.set('basic', 'name', user_name)
        # 初始化数量信息
        conf.set('basic', 'devices_num', 1)
        conf.set('basic', 'cloud_num', 0)
        # 保存信息
        import time
        cfg.set('basic', 'last_modified', time.time())
        save_config(cfg)
        print('Initialization succeeds.')

def tree_nodes_info(level=0):
    #这个方法通过从配置信息中恢复出整个系统的节点情况，给用户查看
    cfg = get_config()
    if level:
        print('You get the infomation!')
        print('Total quota size: XXX MB')
        print('Available quota size(before redundant): XXX MB')
        print('Available quota size(after redundant): XXX MB')
        print('Estimate upload speed: XXX KB/s')
        print('Estimate download speed: XXX KB/s')
    else:
        pass

# # 检查本地节点改动，并更新配置
# def sync_from_local():
#     pass


if __name__ == '__main__':
    print('import succeeds')
