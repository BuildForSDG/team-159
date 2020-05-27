# import json
#
# import django.contrib.auth.models import User
# from django.urls import reverse
from rest_framework import status
# from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


# from accounts.serializers import UsersSerializer
# from accounts.models import User

class UserListTestCase(APITestCase):

    def test_userlist(self):
        data = {"username": "testcase", "email": "test@localhost.app", "password": "some_strong_psw"}
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status=status.HTTP_201_CREATED)
