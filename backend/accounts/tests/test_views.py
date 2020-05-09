import pytest
from django.urls import reverse
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

