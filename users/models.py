# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Account(models.Model):
    """
    Users' accounts
    """
    password = models.CharField(max_length=32, verbose_name='密码')
    username = models.CharField(max_length=16, verbose_name='用户名')
    email = models.EmailField(max_length=64, verbose_name='邮箱')
    state_choice = (('normal', '正常'), ('frozen', '冻结'), ('deleted', '注销'))
    state = models.CharField(choices=state_choice, max_length=32,
                             verbose_name='状态', default='normal')
    role_choice = (('user', '用户'), ('admin', '管理员'))
    role = models.CharField(max_length=32, verbose_name='角色')

    def __unicode__(self):
        return '%s_%s' % (self.username, self.email)


class Profile(models.Model):
    """
    User's profiles
    """
    account = models.ForeignKey(to=Account, related_name='profile_of_user')
    username = models.CharField(max_length=16, verbose_name='用户名')
    sex_choice = (('male', '男'), ('female', '女'))
    sex = models.CharField(choices=sex_choice, max_length=4, blank=True)
    birthday = models.DateField(verbose_name='生日', blank=True)
    address = models.CharField(max_length=128, verbose_name='地址', blank=True)

