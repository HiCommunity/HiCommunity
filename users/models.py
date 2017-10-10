# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Profile(models.Model):
    password = models.CharField(max_length=32, verbose_name='密码')
    username = models.CharField(max_length=16, verbose_name='姓名', blank=True)

    # sex_choice = (('male', '男'), ('female', '女'))
    # sex = models.CharField(choices=sex_choice, max_length=4, blank=True)
    # address = models.CharField(max_length=128, verbose_name='住址', blank=True)

    def __unicode__(self):
        return self.username