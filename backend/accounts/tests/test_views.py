import pytest
from django.urls import reverse
from django.core import mail
from accounts.tests.factories.model_factory import UserFactory
from accounts.models import User

@pytest.mark.django_db
class TestLogin:
    def test_valid_login(self, api_client):
        user = UserFactory(username='test')
        user.set_password('test')
        user.save()
        url = reverse('accounts:token_obtain_pair')
        payload = dict(username='test', password='test')
        result = api_client.post(url, payload)
        assert result.status_code == 200
        assert result.data['access']
        assert result.data['refresh']

    def test_invalid_login(self, api_client):
        url = reverse('accounts:token_obtain_pair')
        payload = dict(username='test', password='invalidpassword')
        result = api_client.post(url, payload)
        assert result.status_code == 401
        assert result.data['detail'] == 'No active account found with the given credentials'


@pytest.mark.django_db
class TestUserRegistration:

    def test_registration(self, api_client):
        url  = reverse('accounts:customers-list')
        username='customer1'
        email='customer1@biz.com'
        first_name = 'customer1'
        last_name = 'loan'
        password='customer1'
        payload =  dict(
            username=username,
            email=email,
            first_name = first_name,
            last_name = last_name,
            password=password
        )
        api_client.post(url, payload)
        
        # ensure the user is in database
        user =  User.objects.get(
            username=username,
            email=email,
            first_name = first_name,
            last_name = last_name,)
        
        assert user.username == username
        assert user.email == email
        assert user.last_name == last_name
        assert user.first_name == first_name
        # ansure user can login
        assert user.check_password(password)

        # test welcome email is sent
        assert len(mail.outbox) == 1