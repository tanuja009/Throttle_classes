from rest_framework import serializers
from .models import *

class studentlistserializer(serializers.ModelSerializer):
  class Meta:
    model=student
    fields=['name','age','subject','gender']

    def validate_age(self, value):
      if value <= 20:
        raise serializers.ValidationError("Age must be greater than 20.")
      return value
    
    def validate(self, data):
        name = data.get('name')
        if not len(name)>5:
            raise serializers.ValidationError("Name and subject cannot be the same.")
        return data

