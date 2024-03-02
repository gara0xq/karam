from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class VecationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vecation
        fields = '__all__'

class BrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brawing
        fields = '__all__'
