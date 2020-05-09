from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'is_staff', 'first_name', 'last_name']

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'first_name', 'last_name', 'password']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data,)