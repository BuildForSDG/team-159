from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Loan(models.Model):
    """
    Customer chosen loans
    """
    # The owner of the account or the owner of the business
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    # status sent or not sent
    status = models.BooleanField()
    # Total amount requested
    amount = models.IntegerField(null=False, blank=False)
    # set durations
    duration = models.IntegerField(null=False, blank=False)
    # loan purpose
    purpose = models.TextField(blank=False, null=False)
    # data placed
    data_placed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer}, {self.amount}"

    class Meta:
        verbose_name = _('Loan')
        verbose_name_plural = _("Loans")
        db_table = "Loan"


class Lender(models.Model):
    """
    Registered Money lenders
    """
    is_lender = models.BooleanField(
        _('is lender'),
        default=False,
    )
    # loan requests to this lender
    loan_requests = models.ManyToManyField(to=Loan)
    # lender name
    name = models.CharField(max_length=30, blank=False, null=False, unique=True)
    # Location
    location = models.CharField(max_length=200, blank=False, null=False, unique=False)
    # Email
    email = models.EmailField(max_length=200, unique=True, blank=False, null=False)
    # lender phone number
    phone_number = models.CharField(max_length=15, unique=True, blank=False, null=False)
    # lender type
    lender_type = models.CharField(max_length=200, blank=False, null=False)
    # lender description
    description = models.TextField(null=False, blank=False)
    # lender website
    website = models.URLField(unique=True)
    # lender Images
    images = models.FileField(upload_to='lender/Images/')
    # lender Certificate
    certificate = models.FileField(upload_to='lender/Certificate/')
    #  date joined
    date_joined = models.DateTimeField(auto_now=True)
    # slug to lender
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('lender')
        verbose_name_plural = _("Lenders")
        db_table = "lender"


class Business(models.Model):
    """
    Business Model - all details of the users business
    """
    # Owner should be the user
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # many loan requests
    loans = models.ManyToManyField(to=Loan)
    # Business number
    business_number = models.CharField(max_length=200, blank=False, null=False, unique=True)
    # Business name
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    # Business type
    business_type = models.CharField(max_length=200, blank=False, null=False)
    # Business email
    email = models.EmailField(max_length=200, unique=True, blank=False, null=False)
    # Business phone number
    phone_number = models.CharField(max_length=15, unique=True, blank=False, null=False)
    # Business location
    location = models.CharField(unique=False, max_length=200, null=False, blank=False)
    # Business description
    description = models.TextField(null=False, blank=False)
    # Business Images
    images = models.FileField(upload_to='Business/Images/')
    # Business Certificate
    certificate = models.FileField(upload_to='Business/Certificate/')
    # business registration
    date_joined = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def cert(self):
        return self.certificate.url

    @property
    def image(self):
        return self.images.url

    class Meta:
        verbose_name = _('Business')
        verbose_name_plural = _("Businesses")
        db_table = "Business"
