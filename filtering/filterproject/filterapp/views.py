from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView
from django.db.models import Q 
from .mypaginations import MyPageNumberPagination


# Create your views here.
class employeelist(ListAPIView):
    # queryset=employee.objects.filter(passby='user')
    queryset = employee.objects.all()
    serializer_class = employeedetailsserializer

    def get_queryset(self):
        
      # return employee.objects.filter(name__istartswith='s').order_by('-name')
     return employee.objects.filter(Q(name__istartswith='s') | Q(salary__gt=30000)).order_by('-name')
    
class paginationview(ListAPIView):
   queryset=student.objects.all()
   serializer_class=studentlistserializer
   pagination_class=MyPageNumberPagination

