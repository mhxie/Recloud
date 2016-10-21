# 模块描述

这个模块专注于Recloud的去服务器化验证登录。

## 先决模块
* Adapter

## 开发阶段

一期：
本地存储，本地配置，客户端之间隔离，专注配置管理

二期：
可选多设备配置同步

三期：
提高配置文件同步的安全性，稳定性

## TO-DO
1. 完成RecloudConfig模块设计，解决校验问题
2. 整理配置文件
3. 完成先决模块Adapter的开发
4. 解决同步冲突问题
5. 解决相对导入问题[已解决]

## 需要Adapter提供的接口
* 类初始化时，输入节点类型

		{
			onedrive: onedrive,
			baiduyun: 百度云,
			googledrive: googledrive,
			local: 本地节点,
			nas: 网络存储,
		}
* 初始化后返回该类的实例
* 实例需要实现包括以下方法：
    * 返回节点的quota[允许列表：]
    * 返回节点的寿命


# Module Description


This module focuses how to distinguish our users without any servers for authentication.

## Prerequisites
* adapter

## Modules in service to
* control_manager
* ui
