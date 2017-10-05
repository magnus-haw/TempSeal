import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.forms import ModelForm
from djgeojson.fields import PointField,PolygonField

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

HOT=2
WARM = 1
JUSTRIGHT = 0
COOL = -1
COLD = -2

TEMPS = (
    (HOT, 'Very Hot!'),
    (WARM, 'Warm'),
    (JUSTRIGHT, 'Just right!'),
    (COOL, 'Cool'),
    (COLD, 'Very Cold!'),
    )

class Building(models.Model):
    name = models.CharField(max_length=100)
    abbrv = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geom = PointField() 
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class SingleResponse(models.Model):    
    timestamp = models.DateTimeField(auto_now_add=True)
    student_ID= models.CharField(max_length=12)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room = models.PositiveIntegerField()
    temp = models.IntegerField(choices=TEMPS,default=JUSTRIGHT)   



