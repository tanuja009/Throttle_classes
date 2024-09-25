from rest_framework import serializers
from .models import *

class studentlistserializer(serializers.ModelSerializer):
  class Meta:
    model=student
    fields=['id','name','age','city','passby']