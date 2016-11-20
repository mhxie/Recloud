# -* - coding: UTF-8 -* -
from configparser import ConfigParser

# if __name__ == '__main__':
#     from adaptor import iadd_adaptor, idel_adaptor, iget_all_adapters
# else:
#     from .adaptor import iadd_adaptor, idel_adaptor, iget_all_adapters
# from adaptor import add_adaptor, del_adaptor, get_all_adapters

# format
# [cloud_<ID>]
# type: {
#       onedrive: onedrive,
# 		baiduyun: 百度云,
# 		googledrive: googledrive,
# 		local: 本地节点,
# 		nas: 网络存储,
#         }
# total_quota: 2048
# available_quota: 1024
# unit: Mb
# expires:
# recover_info:

# class RecloudConfig(ConfigParser):
#     '''Rewrite the ConfigPaser to achieve verificaiton'''
#     def __init__(self):
#         ConfigParser.__init__(self)
#         ConfigParser.read('.recloud.cfg')
#         ConfigParser.add_section('basic')
#         ConfigParser.add('basic', 'name', user_name)
#         ConfigParser.add('basic', 'cloud_num', '0')
#         ConfigParser.add('overview', 'total_quota', '0')
#         ConfigParser.add('overview', 'available_quota', '0')
#         ConfigParser.add('overview', 'unit', 'KB')
#         self.switch = {
#             'basic': basic_sec_verification,
#             'overview': overview_sec_verification
#         }
#     def basic_sec_verification(self, opt, val):
#         # some verification here
#         pass
#     def overview_sec_verification(self):
#         # some verification here
#         pass
#     def completed(self):
#         conf.write(open('.recloud.cfg', 'w'))
#     def set(sec, opt, val):
#         self.switch[sec](opt, val)
#         # some code to deal with exception
#         self.set(sec, opt, val)
#         self.completed()

# 如果同步打开，检查本地配置与云配置的差异，并同步（更新）
def sync_to_cloud():
    pass
# 如果加密打开，尝试对云端的配置进行解密
def sync_from_cloud():
    pass
# 如果存在多个设备时，尝试更新所有云节点的配置
def sync_between_devices():
    # 如果加密关闭：
    # 如果加密打开
    pass

# 以下方法由recloud调用
def update_when_node_deleted(self, node_seq):
    # 当节点被删除时
    # 删除本地对应节点配置
    # 更新overview，打上最新的时间戳
    # 如果开启了配置云同步选项，向云端发起同步请求
    pass

def update_when_node_added(self, node_seq, adaptor):
    # 当新增一个节点时
    info = adaptor.info()
    cfg = ConfigParser.read('.recloud.cfg')
    node_name = 'node_' + node_seq
    # 在本地增加对应节点配置
    cfg.add_section(node_name)
    cfg.set(node_name, 'type', info['type'])
    cfg.set(node_name, 'total_quota', info['Quota'])
    cfg.set(node_name, 'available_quota', info['Used'])
    # 更新overview，打上最新的时间戳
    total_quota = cfg.get('overview', 'total_quota')
    available_quota = cfg.get('overview', 'available_quota')
    cfg.set('overview', 'total_quota', total_quota+info['Quota'])
    cfg.set('overview', 'available_quota', total_quota+info['Used'])
    import time
    cfg.set('basic', 'last_modified', time.time())
    # 如果开启了配置云同步选项，向云端发起同步请求
    if cfg.get('overview', 'sync') == 'on':
        # 调用sys_upload
        # 若同步成功
        if sync_from_cloud():
            sync_between_devices()
        # 若同步失败
        else:
            sync_to_cloud()
    # 新建一个以设备名目录，将本地配置加密分块后上传至该目录
    # 同步时若发现sys目录下已经有一个或多个设备名目录，下面有一个recloud_config_<[0-9]+>的文件包
    #   下载到last_clients目录下的上一个设备名目录尝试解锁
    #       若解锁失败，保留日志
    #       若解锁成功，恢复并更新本地配置

# 检查cfg文件是不是被非法篡改，用于doctor
def self_check():
    pass

# 第一次运行时的初始化
def initialize():
    import os
    if not os.path.exists('.recloud.cfg'):
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
        cfg.write(open('.recloud.cfg', 'w'))
        print('Initialization succeeds.')
def tree_nodes_info(level=0):
    #这个方法通过从配置信息中恢复出整个系统的节点情况，给用户查看
    cfg = ConfigParser()
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



# def add_cloud_node(cloud_type):
#     cloud = Adapter(cloud_type) ## Adapter module needed
#
#     conf = RecloudConfig()
#     conf.read('.recloud.cfg')
#
#     cloud_num = conf.getint("basic", "cloud_num")
#     conf.set("basic", "cloud_num", cloud_num+1)
#
#     new_section_name = 'cloud-'+cloud.getName() ## Adapter module method needed
#     conf.add_section(new_section_name)
#     # conf.add(new_section_name, "???", cloud.get???)
#
#
#     if conf.get("basic", "sync") == "on":
#         autocheck()


if __name__ == '__main__':
    print('import succeeds')
