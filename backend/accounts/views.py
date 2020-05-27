from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class UserList(APIView):
    # permission_classes((IsAuthenticated,))
    def get(self, request):
        model = User.objects.all()
        serializer = UsersSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        # permission_classes((IsAuthenticated,))
        model = User.objects.all()
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    # permission_classes((IsAuthenticated,))
    def get_user(self, National_ID):
        try:
            model = User.objects.get(id=National_ID)
            return model
        except User.DoesNotExist:
            return

    def get(self, request, National_ID):
        if not self.get_user(National_ID):
            return Response(f"User with {National_ID} is not found in the database", status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(self.get_user(National_ID))
        return Response(serializer.data)

    def put(self, request, National_ID):
        serializer = UsersSerializer(self.get_user(National_ID), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, National_ID):
        if not self.get_user(National_ID):
            return Response(f"User with {National_ID} is not found in the database", status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(National_ID)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

