from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class VecationViewSet(viewsets.ModelViewSet):
    queryset = Vecation.objects.all()
    serializer_class = VecationSerializer

class BrawingViewSet(viewsets.ModelViewSet):
    queryset = Brawing.objects.all()
    serializer_class = BrawingSerializer
