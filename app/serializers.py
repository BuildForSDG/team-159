from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LoanSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(
        many=True,
        queryset=Loan.objects.all(),
        slug_field='customer'
    )

    class Meta:
        model = Loan
        fields = "__all__"


class BusinessSerializer(serializers.ModelSerializer):
    # owner = UserSerializer(required=True)
    # loans = LoanSerializer(required=True)

    class Meta:
        model = Business
        fields = "__all__"
        # exclude = "owner"


class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = "__all__"
