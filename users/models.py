# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Profile(models.Model):
    """
    Main users' information
    """
    password = models.CharField(max_length=32, verbose_name='密码')
    username = models.CharField(max_length=16, verbose_name='用户名')
    email = models.EmailField(max_length=64, verbose_name='邮箱')

    def __unicode__(self):
        return '%s_%s' % (self.username, self.email)


class Metadata(models.Model):
    """
    Detailed information of users
    """
    user = models.ForeignKey(to=Profile, related_name='metadata_of_user')
    sex_choice = (('male', '男'), ('female', '女'))
    sex = models.CharField(choices=sex_choice, max_length=4, blank=True)
    birthday = models.DateField(verbose_name='生日', blank=True)
    address = models.CharField(max_length=128, verbose_name='地址', blank=True)

