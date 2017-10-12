# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response


def index(request):
    return render(request, 'common/index.html')

