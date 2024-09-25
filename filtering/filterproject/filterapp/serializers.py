from rest_framework import serializers
from .models import *

class employeedetailsserializer(serializers.ModelSerializer):
  class Meta:
    model=employee
    fields=['id','name','age','salary','domain','passby']