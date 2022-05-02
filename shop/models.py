from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class color(models.Model):
    colores = models.CharField(max_length=32,blank = True , default= 'ali')
    def __str__(self):
        return f'{self.colores}'
class category(models.Model):
    subcategory = models.CharField(max_length=32,blank = True , null=True)
    def __str__(self):
        return f'{self.subcategory}'

class brand(models.Model):
    brandes = models.CharField(max_length=32,blank = True , default= 'ali')
    def __str__(self):
        return f'{self.brandes}'   
    
class product(models.Model):
    name = models.CharField(max_length=32)
    brands = models.ForeignKey (brand,on_delete=models.CASCADE)
    categories = models.ForeignKey (category,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    colors = models.ForeignKey (color,on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    def __str__(self):
        return f'{self.name})'
