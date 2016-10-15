# -* - coding: UTF-8 -* -
from ConfigParser import ConfigParser
from ..adapter import Adapter

class RecloudConfig(ConfigParser):
    '''Rewrite the ConfigPaser to achieve verificaiton'''
    def __init__(self):
        ConfigParser.__init__(self)
        ConfigParser.read('recloud.cfg')
        ConfigParser.add_section('basic')
        ConfigParser.add('basic', 'name', user_name)
        ConfigParser.add('basic', 'cloud_num', '0')
        ConfigParser.add('overview', 'total_storage', '0')
        ConfigParser.add('overview', 'available_storage', '0')
        ConfigParser.add('overview', 'unit', 'Mb')
        self.switch = {
            'basic': basic_sec_verification,
            'overview': overview_sec_verification
        }
    def basic_sec_verification(self, opt, val):
        # some verification here
        pass
    def overview_sec_verification(self):
        # some verification here
        pass
    def set(sec, opt, val):
        self.switch[sec](opt, val)
        # some code to deal with exception
        self.set(sec, opt, val)
        self.completed()

    def completed(self):
        conf.write(open('recloud.cfg', 'w'))

# 第一次运行时的初始化
def initialize():
    conf = RecloudConfig()
    user_name = input("What's your name?\n")
    conf.set("basic", "name", user_name)

    # 获取本机名称

# 检查本地配置与云配置的差异
def sync():
    pass

def add_cloud_node(cloud_type):
    cloud = Adapter(cloud_type) ## Adapter module needed

    conf = RecloudConfig()
    conf.read('recloud.cfg')

    cloud_num = conf.getint("basic", "cloud_num")
    conf.set("basic", "cloud_num", cloud_num+1)

    new_section_name = 'cloud-'+cloud.getName() ## Adapter module method needed
    conf.add_section(new_section_name)
    # conf.add(new_section_name, "???", cloud.get???)


    if conf.get("basic", "sync") == "on":
        autocheck()
