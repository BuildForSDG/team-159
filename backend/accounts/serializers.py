from rest_framework import serializers
from .models import User


class UsersSerializer(serializers.ModelSerializer):
    Username = serializers.CharField(required=False)
    Business_number = serializers.CharField(required=False)
    Email = serializers.EmailField(required=False)
    Full_name = serializers.CharField(required=False)
    National_ID = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = '__all__'
