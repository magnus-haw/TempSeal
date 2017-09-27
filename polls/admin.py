# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Question,Choice,SingleResponse,Building
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Building)

class SingleResponseAdmin(admin.ModelAdmin):
    list_display =('timestamp','student_ID','building','room','temp')
    list_filter = ['timestamp']
    search_fields = ['building__name','student_ID']

admin.site.register(SingleResponse,SingleResponseAdmin)
