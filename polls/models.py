import datetime
from django.db import models
from django.db.models import Count,Avg
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.forms import ModelForm
from djgeojson.fields import PointField,PolygonField

# Create your models here.

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
    temp = models.FloatField(default=JUSTRIGHT)
    food = ""

    def avg_temp(self):
        "get average from SingleResponses"
        q=SingleResponse.objects.filter(building__name = self.name)
        average_temp = q.aggregate(Avg('temp'))['temp__avg']
        if average_temp != None:
            self.temp = int(average_temp)
            self.save()
        return average_temp
    
    def food(self):
        q = foodResponse.objects.filter(building__name = self.name)
        now = datetime.datetime.now()

        if q.endTime < now: #future before past
            self.food = q.food
        else:
            self.food = ""
        self.save()

        return food

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

class foodResponse(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    student_ID= models.CharField(max_length=12)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room = models.PositiveIntegerField()   
    food = models.CharField(max_length=50)
    endTime = models.TimeField() 