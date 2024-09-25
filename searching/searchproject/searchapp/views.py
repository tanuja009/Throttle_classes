from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter

# Create your views here.
class workerslist1(ListAPIView):
  queryset=workers.objects.all()
  serializer_class=workersdetails
  filter_backends=[SearchFilter]
  # search_fields=['area']
  # search_fields=['name','area']
  search_fields=['^name'] #search according to startwith any charactor
  # search_fields=['=name'] #search according to exect match charactor
