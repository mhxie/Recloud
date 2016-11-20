#coding: utf-8


class manager(object):
# 文件管理系统，此系统是整个系统的文件管理层，向下与raid_manager直接相连，中间提供了一个概念上的文件树的管理
    # 文件目录
    list = []
    # 回收站机制
    trash_bin = False
    # 文件查看

    def recover(self):
        pass
        # 在系统重启时，从两个配置文件中恢复出系统结构


    def list(self, path = '/'):
        pass
        #由recloud模块来调用list（）方法，获取文件目录
        #由根目录下来获得，字典，Jason文件，交由系统同步
    #系统文件操作
    def sys_operation(self, device_name, op_code):
        pass
        # note 针对节点而言
        # 相应的设备目录下的系统配置文件操作
        # 下载配置文件的时候无文件映射表，需要自动恢复相应的文件

    def fetch_devices(self):
        pass
        #note 针对节点而言
        #返回sys目录下的所有的子目录的名字
    # 上传
    def upload(self, name, path = '/'):
        pass
        #检查操作
        #调用相应的raid_manager方法来上传文件
        #得到上传成功的回应，然后修改当前文件树
        #如果出错，执行异常处理
    # 下载
    def download(self, path, name):
        pass
        #调用相应的raid_manager方法来下载文件
        #检查文件的完整性

    # 删除文件
    def discard(self, trash_bin):
        pass
        # 调用相应的raid_manager方法来删除
        # 修改当前的文件树
    #返回信息
    def info(self):
        pass
        # 已用容量
        # 剩余容量
        # 总容量信息
    #记录操作信息
    def __log__(self):
        pass
        #记录操作信息
        #操作类型，操作时间，完成时间，操作者
        #

    def exist(self, path = '/', ):
        pass

if __name__ == '__main__':
    pass
    #instance
