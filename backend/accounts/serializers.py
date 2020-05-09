from rest_framework import serializers
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'is_staff', 'first_name', 'last_name']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'first_name', 'last_name', 'password']
    
    def create(self, validated_data):
        user =  User.objects.create_user(**validated_data,)

        # TODO: make email sending async
        subject = 'Subject'
        html_message = render_to_string('accounts/customer_welcome.html', {'user': user})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = user.email

        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

        return user