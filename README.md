# HiCommunity

## 设计理念
* 易扩展，松耦合

* 符合Python、Django设计理念

## 编码规范
* 前端参考http://codeguide.bootcss.com/
* HTML和CSS缩进使用2个空格，可在PyCharm或其他IDE中设置


* 后台参考PEP8。
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
* Django 1.11 / 2.0 in future
* MaterialCSS / Bootstrap4

## 功能
0. 整体（后台管理页面）
* 配置：全局配置，APP配置（py、yaml等）
* 板块：添加、修改或删除

1. 用户
* 角色：普通用户，管理员，系统管理员等
* 权限：在角色允许范围内设置权限
* 注册：普通注册，邮箱验证注册
* 登陆：普通登陆，验证码登陆
* 设置：个人资料，密码修改，头像设置，其他
* 用户详情：待定
* 其他

2. 主题
* 发布
* 回答
* 回答有无帮助
* 回答的回复
* 关闭
* 其他

## 数据库
* 后端使用MySQL

* 表结构（见models.py）

## 数据格式
* 除GET外，其余返回JSON格式，具体格式见common/constants/common.py

## 测试流程
0. 安装依赖包
* pip install mysqlclient
* pip install Pillow
1. 安装并启动MySQL服务
2. 修改settings.py文件中“DATABASES”各项
3. 初始化数据库，在项目根目录依次执行如下命令
* python manage.py makemigrations
* python manage.py migrations
4. 执行sqls/test.sql中的SQL语句（临时构建问答社区的区域板块结构，后续会做管理平台）
5. 启动Django

## 测试注意事项
由于初期数据库修改可能较多，改动较大，如果迁移时出错，可以直接删除库，
并（一定要）删除所有APP目录下的migrations目录中除__init__.py外的所有文件，
然后在执行数据库初始化。
