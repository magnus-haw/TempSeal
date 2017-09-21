# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Question,Choice,SingleResponse,Building
admin.site.register(Choice)
admin.site.register(Question)

admin.site.register(SingleResponse)
admin.site.register(Building)
