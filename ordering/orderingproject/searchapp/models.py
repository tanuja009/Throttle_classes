from django.db import models

# Create your models here.
class workers(models.Model):
  area=[('chemical','chemical'),('mechanical','mechanical'),('scientist','scientist')]
  name=models.CharField(max_length=50)
  area=models.CharField(max_length=50,choices=area)
  salary=models.BigIntegerField()