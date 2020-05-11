from django.test import TestCase, RequestFactory
from accounts.models import Business, User
from accounts.views import (
    NewBusiness
)


class BusinessTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.business = Business.objects.create(
            owner=User.objects.get(id=1),
            name="uwezo",
            business_type="communication",
            business_number="1234567890",
            email="joseph@gmail.com",
            location="Nairobi",
            description="my description",
            phone_number="07121212121"
        )

    def test_create_business(self):
        request = self.factory.get("/new")
        request.user = self.business.owner
        response = NewBusiness.as_view()(request)
        self.assertEqual(response.status_code, 200)

