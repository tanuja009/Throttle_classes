from django.db import models

# Create your models here.
class employee(models.Model):
  domains=[('SW','software developer'),('FD','FrontDeveloper'),('FullStack','FullStack Developer'),('DS','Data Scientist')]
  name=models.CharField(max_length=50)
  age=models.IntegerField()
  salary=models.BigIntegerField()
  domain=models.CharField(max_length=50,choices=domains)
  passby=models.CharField(max_length=100,blank=True)


class student(models.Model):
  name=models.CharField(max_length=50)
  roll_no=models.BigIntegerField()