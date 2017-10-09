# HiCommunity

## 设计理念
* 易扩展，松耦合

* 符合Python、Django设计理念

## 编码规范
* 前端参考http://codeguide.bootcss.com/
* HTML和CSS缩进使用2个空格，可在PyCharm或其他IDE中设置


* 后台参考PIPE8。
* IDE推荐使用PyCharm。
* 如果一行太长，使用软换行（加括号），例如：
`from django.views.generic.detail import (
    BaseDetailView, SingleObjectMixin, SingleObjectTemplateResponseMixin,
)`。
* 核心代码添加详细注释，函数、类、文件添加文档注释。
* 文件编码指定统一使用 `# coding=utf-8`。
* 多个文件引用的模块或函数作为公用方法单独存放，注意目录结构合理性，防止循环引入。

## 框架
* Python 3
* Django 1.11
* MaterialCSS（待定）

## 功能
0. 整体（考虑单独做后台管理页面）
* 配置：全局配置，APP配置（py、yaml等）
* 板块：添加、修改或删除

1. 用户
* 角色：普通用户，管理员，系统管理员等
* 权限：在角色允许范围内设置权限
* 注册：普通注册，邮箱验证注册
* 登陆：普通登陆，验证码登陆
* 设置：个人资料，密码修改，头像设置，其他
* 用户详情：待定

2. 主题
* 发布
* 回答
* 回答有无帮助
* 回答的回复
* 关闭

## 数据库
* 后端使用MySQL

* 表结构（待定）

## 数据格式
* 待定