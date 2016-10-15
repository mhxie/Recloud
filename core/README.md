# README

[中文介绍]

这个文件夹作为项目初期按模块开发方便整理使用，后期会聚合大家的代码，并将各部分文档整理到根目录下的docs里。

命令行版本使用介绍：

`python3 recloud.py help` # 查看帮助

`python3 recloud.py login` # 登录新账户

`python3 recloud.py info` # 查看账户信息

`python3 recloud.py conf` # 修改配置

`python3 recloud.py upload [file_from] [file_to]` # 上传文件，默认根目录

`python3 recloud.py download [file_from] [file_to]` # 下载文件，默认当前目录

`python3 recloud.py tree` # 打印出当前文件树

`python3 recloud.py doctor` # 检查云的健康情况

开发阶段划分：

一期：单云盘单账户，文件加密，配置文件本地存储

二期：多云盘单账户，文件冗余

三期：多云盘多账户，配置文件云存储

四期：bug修改，性能优化

五期：Web UI开发

六期：上传/下载多线程，多客户端支持


[English]

This folder is created for raw code of the core of the system. The subfolders are created temporarily for developing. After first developing phase, they will be restructured to a cleaner appearance.