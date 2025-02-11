from django.db import models

# Create your models here.
class Propertie (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=False, null=False, default='')
    sellType= models.CharField(max_length=100, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    condoPrice = models.FloatField(blank=True, null=True)
    iptuPrice = models.FloatField(blank=True, null=True)
    fullAddress = models.CharField(max_length=250, blank=False, null=False, default='')
    neighborhood = models.CharField(max_length=100, blank=False, null=False, default='')
    city = models.CharField(max_length=100, blank=False, null = False, default='')
    state = models.CharField(max_length=100, blank=False, null=False, default='')
    description = models.CharField(max_length=500, blank=False, null=False, default='')
    infos = models.CharField(max_length=10000, blank=False, null=False, default='')
    link = models.CharField(max_length=100, null=False, blank=False, default='')


    def __str__(self):
        return self.name