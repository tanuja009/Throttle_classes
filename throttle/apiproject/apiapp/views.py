from rest_framework import viewsets
from .models import student
from .serializers import studentlistserializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

# Create your views here.
class apiclasses1(viewsets.ModelViewSet):
  queryset=student.objects.all()
  serializer_class=studentlistserializer
  authentication_classes=[SessionAuthentication]
  permission_classes=[IsAuthenticatedOrReadOnly]
  throttle_classes=[AnonRateThrottle,UserRateThrottle]
