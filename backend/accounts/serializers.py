from rest_framework import serializers
from .models import (User, Business)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'first_name', 'last_name']


class BusinessSerializer(serializers.ModelSerializer):
    manager = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='business-detail')

    class Meta:
        model = Business
        fields = "__all__"

