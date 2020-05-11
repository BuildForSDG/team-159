from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass


class Business(models.Model):
    """
    Business Model - all details of the users business
    """
    # Owner should be the user
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Business number
    business_number = models.CharField(max_length=200, blank=False, null=False, unique=True)
    # Business name
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    # Business type
    business_type = models.CharField(max_length=200, blank=False, null=False)
    # Business email
    email = models.EmailField(max_length=200, unique=True, blank=False, null=False)
    # Business phone number
    phone_number = models.CharField(max_length=200, unique=True, blank=False, null=False)
    # Business location
    location = models.CharField(unique=False, max_length=200, null=False, blank=False)
    # Business description
    description = models.TextField(null=False, blank=False)
    # Business Images
    images = models.FileField(upload_to='Business/Images/')
    # Business Certificate
    certificate = models.FileField(upload_to='Business/Certificate/')

    def __str__(self):
        return self.name

    def cert(self):
        return self.certificate.url

    def image(self):
        return self.images.url

    def get_absolute_url(self):
        return reverse('accounts:read', kwargs={'pk': self.id})

    class Meta:
        verbose_name = _('Business')
        verbose_name_plural = _("Businesses")
