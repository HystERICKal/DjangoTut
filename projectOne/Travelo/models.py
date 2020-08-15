from django.db import models

# Create your models here.


class Destination(models.Model):
    #id:int
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'pics')