import datetime
import json
from app.models import Business, User, Lender, Loan
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from mixer.backend.django import mixer


class BusinessTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test", email="test@gmail.com", password="i_am_git")
        self.token = Token.objects.create(user=self.user)
        self.created_user = User.objects.get(username="test")
        self.token = Token.objects.create(user=self.user)
        self.api_Authentication()
        self.random = User.objects.create_user(username="testhack", email="testhack@gmail.com",
                                               password="i_am_not_joseph")

        self.name = "uwezo"
        self.add_business = reverse("add-business")
        self.update_business = reverse("update-business", kwargs={"name": self.name})
        self.delete_business = reverse("delete-business", kwargs={"name": self.name})
        self.business = mixer.blend(
            Business,
            name="random",
            owner=self.random,
        )
        self.data = {
            "name": f"{self.name}",
            "owner": f"{self.user}",
            "business_number": "0171918289",
            "business_type": f"{self.business.business_type}",
            "email": "uwezo@gmail.com",
            "phone_number": "0716018181",
            "location": f"{self.business.location}",
            "description": f"{self.business.description}",
            "images": f"{self.business.images}",
            "date_joined": f"{datetime.datetime}",
            "last_modified": f"{datetime.datetime}",
            "certificate": f"{self.business.certificate}",
        }

    def api_Authentication(self):
        """
        Create an authentications token for the created user
        """
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_can_retrieve_business_as_authenticated(self):
        """
        Test that the authenticated user can retrieve data specific to them
        """
        response = self.client.get(self.add_business)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_can_retrieve_business_as_not_authenticated(self):
        """
        Test that an  unauthenticated user can retrieve data specific to them
        """
        self.client.force_authenticate(user=None)
        response = self.client.get(self.add_business, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_create_business(self):
        """
        An authenticated user can create their business profile
        """
        response = self.client.post(self.add_business, data=self.data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_create_business_by_random_owner(self):
        """
        An unauthenticated user cannot create their business profile
        """
        random = User.objects.create_user(username="testhack", email="testhack@gmail.com", password="i_am_not_joseph")
        self.client.force_authenticate(user=random)
        response = self.client.post(self.add_business, data=self.data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 0)

    def test_can_update_business_by_owner(self):
        """
        An authenticated user can update their business profile
        """
        response = self.client.get(reverse("update-business", kwargs={"name": self.business}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.put(reverse("update-business", kwargs={"name": self.business}),
                                   data={"name": "new business name"}, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_business_by_random_owner(self):
        """
        An unauthenticated user can update an existing business profile
        """
        self.client.force_authenticate(user=self.random)
        response = self.client.put(reverse("update-business", kwargs={"name": self.business}),
                                   data={"name": "new business name"}, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 0)

    def test_can_delete_business_by_owner(self):
        """
        An authenticated Staff member can delete a business profile
        """
        response = self.client.get(reverse("delete-business", kwargs={"name": self.business}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(reverse("update-business", kwargs={"name": self.business}),
                                      content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_delete_business_by_random_owner(self):
        """
        An unauthenticated Staff member can delete a business profile
        """
        self.client.force_authenticate(user=self.random)
        response = self.client.put(reverse("update-business", kwargs={"name": self.business}),
                                   content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 0)


class LoanTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", email="test@gmail.com", password="i_am_git")
        self.token = Token.objects.create(user=self.user)
        # self.loan = mixer.blend(Loan, customer=self.user)
        self.data = {
            "customer": f"{self.user}",
            "status": "False",
            "amount": "10000",
            "duration": "12",
            "purpose": "Add a new store",
        }
        self.update_data = {
            "customer": f"{self.user}",
            "status": "False",
            "amount": "1000",
            "duration": "1",
            "purpose": "Add a new store and a shop",
        }
        self.update_random_data = {
            "customer": f"{self.random}",
            "status": "False",
            "amount": "1000",
            "duration": "1",
            "purpose": "Add a new store and a shop",
        }
        self.random_data = {
            "customer": f"{self.random}",
            "status": "False",
            "amount": "10000",
            "duration": "12",
            "purpose": "Add a new store",
        }
        self.api_Authentication()
        self.add_loan = reverse("add-loan")
        self.delete_loan = reverse("delete-loan", kwargs={"customer": self.data["customer"]})
        self.update_loan = reverse("update-loan", kwargs={"customer": self.data["customer"]})
        self.random = User.objects.create_user(username="testhack", email="testhack@gmail.com",
                                               password="i_am_not_joseph")

    def api_Authentication(self):
        """
        Create an authentications token for the created user
        :return: None
        """
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_can_retrieve_loan_data_as_authenticated(self):
        """
        An authenticated user/Client can retrieve a loan request data[specific]
        :return:
        """
        response = self.client.get(self.add_loan)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # no related loan created to Business in this instance

    def test_can_retrieve_loan_data_as_unauthenticated(self):
        """
        An unauthenticated user/Client cannot retrieve a loan request data
        :return:
        """
        self.client.force_authenticate(user=self.random)
        response = self.client.get(self.add_loan)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 0)

    def test_can_create_loan_as_authenticated(self):
        """
        An authenticated user/Client can create a loan request
        :return:
        """
        response = self.client.post(self.add_loan, data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 1)

    def test_can_create_loan_as_unauthenticated(self):
        """
        An unauthenticated user/Client cannot create a loan request
        :return:
        """
        self.client.force_authenticate(user=self.random)
        response = self.client.post(self.add_loan, data=json.dumps(self.random_data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_update_loan_as_authenticated(self):
        """
        An authenticated user/Client can update a loan request data
        :return:
        """
        response = self.client.put(self.update_loan, data=json.dumps(self.update_data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_can_update_loan_as_unauthenticated(self):
        """
        An unauthenticated user/Client cannot update a loan request data
        :return:
        """
        self.client.force_authenticate(user=self.random)
        response = self.client.put(self.update_loan, data=json.dumps(self.update_random_data),
                                   content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_loan_as_authenticated(self):
        """
        An authenticated Staff member can delete a loan request on request
        :return:
        """
        response = self.client.delete(self.delete_loan, data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 1)

    def test_can_delete_loan_as_unauthenticated(self):
        """
        An unauthenticated Staff member cannot delete a loan request
        :return:
        """
        self.client.force_authenticate(user=self.random)
        response = self.client.delete(self.delete_loan, data=json.dumps(self.random_data),
                                      content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# class LenderTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.lender = mixer.blend(Lender)
