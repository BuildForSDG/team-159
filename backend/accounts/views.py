from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer,CustomerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer