import factory
from accounts.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'accounts.User'
        
    username = factory.sequence(lambda n:n)
    