from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
# Create your views here.

class studentlist(ListAPIView):
  queryset=student.objects.all()
  # queryset=student.objects.filter(passby='user')
  serializer_class=studentlistserializer
  
