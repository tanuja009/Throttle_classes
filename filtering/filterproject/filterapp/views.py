from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView

# Create your views here.
class employeelist(ListAPIView):
    # queryset=employee.objects.filter(passby='user')
    queryset = employee.objects.all()
    serializer_class = employeedetailsserializer

    def get_queryset(self):
        
      return employee.objects.filter(name__istartswith='s')