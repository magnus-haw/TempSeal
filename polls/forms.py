from django import forms
from .models import SingleResponse

class ResponseForm(forms.ModelForm):
    class Meta:
        model = SingleResponse
        fields = ['student_ID', 'building', 'room', 'temp']
