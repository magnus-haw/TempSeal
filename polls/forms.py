from django import forms
from django.db import models
from leaflet.forms.widgets import LeafletWidget
from .models import SingleResponse, foodResponse

class FoodForm(forms.ModelForm):
    class Meta:
        model = foodResponse
        fields = ('student_ID','building','food')
        exclude= ('geom',)

class ResponseForm(forms.ModelForm):
    class Meta:
        model = SingleResponse
        fields = ['email', 'building', 'room', 'temp','comment']

