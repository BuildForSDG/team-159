from django.db import models, migrations

from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token



class User(AbstractUser):
    phone_number = models.CharField(max_length=30, default=254)
    business_number = models.CharField(default='568', max_length=50)
    national_id = models.CharField(max_length=15, default='01')
    # email = models.EmailField(default='name@gmail.com')

    class Meta:
        db_table = 'user'

    operations = [
        migrations.AddField('user', 'phone_number', models.CharField(default='254')),
        migrations.AddField('user', 'business_number', models.CharField(default='568', max_length=50)),
        migrations.AddField('user', 'national_id', models.CharField(max_length=15)),
        # migrations.AddField('user', 'email', models.CharField(default='name@gmail.com')),
    ]
