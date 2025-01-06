from django.contrib.auth.models import User
from .models import Athlete
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ['name', 'sport']
    
