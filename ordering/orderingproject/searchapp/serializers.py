from rest_framework import serializers
from .models import *

class workersdetails(serializers.ModelSerializer):
  class Meta:
    model=workers
    fields=['id','name','area','salary']