import pytest
from django.urls import reverse
from business.models import Lender
@pytest.mark.django_db
class TestLernder:
    def test_lender_registration(self, api_client):
        
        url = reverse('businesss:lender-list')
        payload = dict(
            business_number='0001', 
            lender_name='lender',
            email='lender@mail.com',
            phone_number='25470000000',
            location='Nairobi',
            description='yes we can',
            minimum_lending_amount=100,
            maxmum_lending_amount=1000000
        )
        result = api_client.post(url, payload)
        assert result.status_code == 201
        lender = Lender.objects.first()
        assert lender.business_number=='0001'
        assert lender.lender_name=='lender'
        assert lender.email=='lender@mail.com'
        assert lender.phone_number=='25470000000'
        assert lender.location=='Nairobi'
        assert lender.description=='yes we can'
        assert lender.minimum_lending_amount==100
        assert lender.maxmum_lending_amount==1000000