from django.db import models
from datetime import date

# Create your models here.
class singer(models.Model):
    name  = models.CharField(max_length=90)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(singer,on_delete=models.CASCADE,related_name='song')
    duration = models.IntegerField()


    def __str__(self):
        return self.title


