from django.test import TestCase, RequestFactory
from mixer.backend.django import mixer

from accounts.models import Business, User
from accounts.views import (
    NewBusiness
)


class BusinessTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.business = mixer.blend(Business)

    def test_create_business(self):
        request = self.factory.get("/new")
        request.user = self.business.owner
        response = NewBusiness.as_view()(request)
        self.assertEqual(response.status_code, 200)

