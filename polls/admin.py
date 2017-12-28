# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

from .models import SingleResponse,Building

class SingleResponseAdmin(admin.ModelAdmin):
    list_display =('timestamp','email','building','room','temp')
    list_filter = ['timestamp']
    search_fields = ['building__name','email']

admin.site.register(SingleResponse,SingleResponseAdmin)

class BuildingAdmin(LeafletGeoAdmin):
    list_display =('name','abbrv','latitude','longitude')
    search_fields = ['name','latitude','longitude']

admin.site.register(Building,BuildingAdmin)
