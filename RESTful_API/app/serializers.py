from rest_framework import serializers
from app.models import employeers

class employeesSerializer(serializers.ModelSerializer):
    class Meta():
        model = employeers
        fields = '__all__'
