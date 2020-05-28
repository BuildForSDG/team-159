from app.models import *
from django.test import TestCase
from mixer.backend.django import mixer


def const_null_blank(self, const, verbose, not_verbose):
    """
    :param self:
    :param const:
    :param verbose:
    :param not_verbose:
    :return:
    """
    label = const.verbose_name
    self.assertEquals(label, verbose)
    self.assertNotEquals(label, not_verbose)
    null = const.null
    self.assertEquals(type(null), bool)
    self.assertEquals(null, False)
    blank = const.blank
    self.assertEquals(type(blank), bool)
    self.assertEquals(blank, False)


def unique_max(self, const, maxL, verbose, not_verbose, uniq=True):
    """
    :param self:
    :param const:
    :param maxL:
    :param verbose:
    :param not_verbose:
    :param uniq:
    :return: None
    """
    const_null_blank(self, const, verbose, not_verbose)
    self.assertEquals(const.unique, uniq)
    self.assertEquals(const.max_length, maxL)

class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name="Joseph", last_name="Gitau")
        
    def test_setup_data_created(self):
        self.assertEquals(User.objects.count(), 1)
        self.assertNotEquals(User.objects.count(), 0)

    def setUp(self): 
        self.first = User.objects.get(id=1)
    
    def test_object_name(self):
        """
        Test __str__ returns f"{self.first.first_name}, {self.first.last_name}"
        :return: None
        """
        self.assertEquals(str(self.first), f"{self.first.first_name}, {self.first.last_name}")
        self.assertNotEquals(str(self.first), f"{self.first.first_name}, {self.first.last_name}.....")
        
   def test_last_name_label(self):
        label = self.first._meta.get_field(field_name="last_name")
        self.assertEquals(type(self.first.last_name), str)
        self.assertEquals(label.max_length, 30)
        const_null_blank(self, verbose="last name", not_verbose="last_name", const=label)
        
   def test_first_name_label(self):
        label = self.first._meta.get_field(field_name="first_name")
        self.assertEquals(type(self.first.first_name), str)
        self.assertEquals(label.max_length, 30)
        const_null_blank(self, verbose="first name", not_verbose="first_name", const=label)
        
   def test_national_id_label(self):
        label = self.first._meta.get_field(field_name="national_id")
        self.assertEquals(label.max_length, 30)
        const_null_blank(self, verbose="national_id", not_verbose="national_id", const=label)
        
   def test_business_number_label(self):
        label = self.first._meta.get_field(field_name="business_number")
        self.assertEquals(label.max_length, 30)
        const_null_blank(self, verbose="business number", not_verbose="business_number", const=label)
    
    def test_email_label(self):
        """
        Test Email field
        :return: None
        """
        self.assertEquals(type(self.first.email), str)
        self.assertEquals(self.first.email, "joseph@gmail.com")
        self.assertNotEquals(self.first.email, "joseph@gmail.co")
        self.assertIn("@gmail.com", self.first.email)
        const = self.first._meta.get_field(field_name="email")
        self.assertNotEquals(const.verbose_name, "email_")
        unique_max(self, const, maxL=200, verbose="email", not_verbose="emailing")
    
    def test_get_username_func(self):
        self.assertEquals(self.first.get_username, None)
        
class LoanModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Setting up of the data
        :return: None
        """
        user = User.objects.create_user(username="team", email="team@gmail.com", password="50391798po")
        Loan.objects.create(customer=user, status=False, amount=1000, duration=10, purpose="More money")

    def setUp(self):
        self.first = Loan.objects.get(id=1)

    def test_created_one_object(self):
        """
        Test that only one Loan is stored in the database
        :return: None
        """
        self.assertEquals(Loan.objects.all().count(), 1)
        self.assertNotEquals(Loan.objects.all().count(), 2)

    def test_object_name(self):
        """
        Test __str__ returns f"{self.first.customer}, {self.first.amount}"
        :return: None
        """
        self.assertEquals(str(self.first), f"{self.first.customer}, {self.first.amount}")
        self.assertNotEquals(str(self.first), f"{self.first.customer}, {self.first.amount}.....")

    def test_customer_label(self):
        """
        Test customer field
        ::
            verbose_name = "customer"
            :type: Customer == User
        :return: None
        """
        label = self.first._meta.get_field(field_name="customer").verbose_name
        self.assertEquals(type(self.first.customer), User)
        self.assertEquals(label, "customer")

    def test_status_label(self):
        """
        Test status field
        :return: None
        """
        const = self.first._meta.get_field(field_name="status")
        self.assertEquals(type(self.first.status), bool)
        const_null_blank(self, const, verbose="status", not_verbose="statuss")

    def test_amount_label(self):
        """
        Test Amount field
        :return: None
        """
        const = self.first._meta.get_field(field_name="amount")
        self.assertEquals(type(self.first.amount), int)
        const_null_blank(self, const, verbose="amount", not_verbose="amounts")

    def test_duration_label(self):
        """
        Test duration field
        :return: None
        """
        const = self.first._meta.get_field(field_name="duration")
        self.assertEquals(type(self.first.duration), int)
        const_null_blank(self, const, verbose="duration", not_verbose="dusratuons")

    def test_purpose_label(self):
        """
        Test purpose field
        :return: None
        """
        const = self.first._meta.get_field(field_name="purpose")
        const_null_blank(self, const, verbose="purpose", not_verbose="iiax")


class LenderModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Testing data set up
        :return: None
        """
        user = User.objects.create_user(username="team", email="team@gmail.com", password="50391798po")
        loan = Loan.objects.create(customer=user, status=False, amount=1000, duration=10, purpose="More money")
        mixer.blend(Lender, loan_requests=loan, is_lender=True, name="Equity", location="Nairobi, Kenya",
                    email="equity@gmail.com", phone_number="071234568", lender_type="Bank",
                    description="Were are a bank", website="https://equity.com", slug="fly-reality-do")

    def setUp(self) -> None:
        self.first = Lender.objects.get(id=1)

    def test_created_one_object(self):
        """
        Test that only one Lender is stored in the database
        :return: None
        """
        self.assertEquals(Lender.objects.all().count(), 1)
        self.assertNotEquals(Lender.objects.all().count(), 2)

    def test_object_name(self):
        """
        Test __str__ returns "Equity"
        :return: None
        """
        self.assertEquals(str(self.first), "Equity")
        self.assertNotEquals(str(self.first), "Equitys")

    def test_is_lender_label(self):
        """
        Test is_lender field
        :return: None
        """
        self.assertEquals(type(self.first.is_lender), bool)
        self.assertEquals(self.first.is_lender, True)
        const = self.first._meta.get_field(field_name="is_lender")
        label = const.verbose_name
        self.assertEquals(label, "is lender")
        default = const.default
        self.assertEquals(type(default), bool)
        self.assertEquals(default, False)

    def test_name_label(self):
        """
        Test name field
        :return: None
        """
        self.assertEquals(self.first.name, "Equity")
        self.assertNotEquals(self.first.name, "Equit")
        self.assertEquals(type(self.first.name), str)
        const = self.first._meta.get_field(field_name="name")
        self.assertNotEquals(const.verbose_name, "equity_")
        unique_max(self, const, maxL=30, verbose="name", not_verbose="naming")

    def test_loan_requests_label(self):
        """
        Test only one loan related to this lender
        :return: None
        """
        self.assertEquals(self.first.loan_requests.count(), 1)

    def test_location_label(self):
        """
        Test Location field
        :return: None
        """
        self.assertEquals(type(self.first.location), str)
        self.assertEquals(self.first.location, "Nairobi, Kenya")
        self.assertNotEquals(self.first.location, "Nairobi, Keny")
        const = self.first._meta.get_field(field_name="location")
        self.assertNotEquals(const.verbose_name, "location_")
        unique_max(self, const, maxL=200, uniq=False, verbose="location", not_verbose="locale")

    def test_email_label(self):
        """
        Test Email field
        :return: None
        """
        self.assertEquals(type(self.first.email), str)
        self.assertEquals(self.first.email, "equity@gmail.com")
        self.assertNotEquals(self.first.email, "equity@gmail.co")
        self.assertIn("@gmail.com", self.first.email)
        const = self.first._meta.get_field(field_name="email")
        self.assertNotEquals(const.verbose_name, "email_")
        unique_max(self, const, maxL=200, verbose="email", not_verbose="emailing")

    def test_phone_number_label(self):
        """
        Test Phone Number field
        :return: None
        """
        self.assertEquals(self.first.phone_number, "071234568")
        self.assertNotEquals(self.first.phone_number, "0712345682")
        const = self.first._meta.get_field(field_name="phone_number")
        self.assertNotEquals(const.verbose_name, "phone_number")
        unique_max(self, const, maxL=15, verbose="phone number", not_verbose="phone_number")

    def test_lender_type_label(self):
        """
        Test Lender Type field
        :return: None
        """
        self.assertEquals(self.first.lender_type, "Bank")
        self.assertNotEquals(self.first.lender_type, "Banks")
        const = self.first._meta.get_field(field_name="lender_type")
        self.assertNotEquals(const.verbose_name, "lender_type")
        unique_max(self, const, maxL=200, uniq=False, verbose="lender type", not_verbose="lenders")

    def test_description_label(self):
        """
        Test Description field
        :return: None
        """
        self.assertEquals(self.first.description, "Were are a bank")
        self.assertNotEquals(self.first.description, "Were are a banks")
        const = self.first._meta.get_field(field_name="description")
        self.assertNotEquals(const.verbose_name, "descriptions")
        unique_max(self, const, maxL=None, uniq=False, verbose="description", not_verbose="descriptions")

    def test_website_label(self):
        """
        Test Url field
        :return: None
        """
        self.assertEquals(self.first.website, "https://equity.com")
        self.assertNotEquals(self.first.website, "http://equity.com")
        self.assertIn("https://", self.first.website)
        self.assertIn(".com", self.first.website)
        const = self.first._meta.get_field(field_name="website")
        self.assertNotEquals(const.verbose_name, "websites")
        unique_max(self, const, maxL=200, uniq=True, verbose="website", not_verbose="websites")

    def test_slug_label(self):
        """
        Test Slug field
        :return: None
        """
        self.assertEquals(self.first.slug, "fly-reality-do")
        self.assertNotEquals(self.first.slug, "Equity")
        const = self.first._meta.get_field(field_name="slug")
        self.assertNotEquals(const.verbose_name, "slugs")
        unique_max(self, const, maxL=200, uniq=True, verbose="slug", not_verbose="slugging")

    def file_image_certificate(self, verbose, not_verbose, maxL=100):
        """
        :param verbose:
        :param not_verbose:
        :param maxL:
        :return:
        """
        const = self.first._meta.get_field(field_name=verbose)
        self.assertNotEquals(const.verbose_name, not_verbose)
        self.assertEquals(const.verbose_name, verbose)
        self.assertEquals(const.max_length, maxL)

    def test_images_label(self):
        """
        Test image url returned
        :return: None
        """
        self.file_image_certificate(verbose="images", not_verbose="image")

    def test_certificate_label(self):
        """
        Test image url returned
        :return: None
        """
        self.file_image_certificate(verbose="certificate", not_verbose="certificates")


class BusinessModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Testing data set up
        :return:
        """
        user = User.objects.create_user(username="team", email="team@gmail.com", password="50391798po")
        loan = Loan.objects.create(customer=user, status=False, amount=1000, duration=10, purpose="More money")
        mixer.blend(Business, owner=user, loans=loan, business_number="1234567890", name="m-uwezo",
                    business_type="Communications", email="uwezo@gmail.com", phone_number="07161181",
                    location="Nakuru, Kenya", description="Our description")

    def setUp(self) -> None:
        self.first = Business.objects.get(id=1)

    def test_created_one_object(self):
        """
        Test that only one Business is stored in the database
        :return: None
        """
        self.assertEquals(Business.objects.all().count(), 1)
        self.assertNotEquals(Business.objects.all().count(), 2)

    def test_object_name(self):
        """
        Test __str__ returns "m-uwezo"
        :return: None
        """
        self.assertEquals(str(self.first), "m-uwezo")
        self.assertNotEquals(str(self.first), "M-Uwezo Club")

    def test_business_number_label(self):
        """
        Test Business Number Field
        :return:
        """
        self.assertEquals(self.first.business_number, "1234567890")
        self.assertNotEquals(self.first.business_number, "123456789")
        const = self.first._meta.get_field(field_name="business_number")
        unique_max(self, const=const, maxL=200, verbose="business number", not_verbose="business_numbers")

    def test_name_label(self):
        """
        Test Business Name Field
        :return:
        """
        self.assertEquals(self.first.name, "m-uwezo")
        self.assertNotEquals(self.first.name, "m-uwezos")
        const = self.first._meta.get_field(field_name="name")
        unique_max(self, const=const, maxL=200, verbose="name", not_verbose="names")

    def test_email_label(self):
        """
        Test Business Email Field
        :return:
        """
        self.assertEquals(self.first.email, "uwezo@gmail.com")
        self.assertNotEquals(self.first.email, "uweso@gmail.com")
        self.assertIn("@gmail.com", self.first.email)
        const = self.first._meta.get_field(field_name="email")
        unique_max(self, const=const, maxL=200, verbose="email", not_verbose="emails")

    def test_business_type_label(self):
        """
        Test Business Type Field
        :return:
        """
        self.assertEquals(self.first.business_type, "Communications")
        self.assertNotEquals(self.first.business_type, "communication")
        const = self.first._meta.get_field(field_name="business_type")
        unique_max(self, const=const, maxL=200, verbose="business type", not_verbose="business_types", uniq=False)

    def test_phone_number_label(self):
        """
        Test Business Phone Number Field
        :return:
        """
        self.assertEquals(self.first.phone_number, "07161181")
        self.assertNotEquals(self.first.phone_number, "07161181323")
        const = self.first._meta.get_field(field_name="phone_number")
        unique_max(self, const=const, maxL=15, verbose="phone number", not_verbose="phone_numbers")

    def test_location_label(self):
        """
        Test Business Location Field
        :return:
        """
        self.assertEquals(self.first.location, "Nakuru, Kenya")
        self.assertNotEquals(self.first.location, "Nakuru, Keny")
        const = self.first._meta.get_field(field_name="location")
        self.assertNotEquals(const.verbose_name, "location_")
        unique_max(self, const, maxL=200, uniq=False, verbose="location", not_verbose="locale")

    def test_description_label(self):
        """
        Test Business Description Field
        :return:
        """
        self.assertEquals(self.first.description, "Our description")
        self.assertNotEquals(self.first.description, "Were are a banks")
        const = self.first._meta.get_field(field_name="description")
        self.assertNotEquals(const.verbose_name, "descriptions")
        unique_max(self, const, maxL=None, uniq=False, verbose="description", not_verbose="descriptions")

    def file_image_certificate(self, verbose, not_verbose, maxL=100):
        """
        :param verbose:
        :param not_verbose:
        :param maxL:
        :return: None
        """
        const = self.first._meta.get_field(field_name=verbose)
        self.assertNotEquals(const.verbose_name, not_verbose)
        self.assertEquals(const.verbose_name, verbose)
        self.assertEquals(const.max_length, maxL)

    def test_images_label(self):
        """
        Test Business Description Field
        :return:
        """
        self.file_image_certificate(verbose="images", not_verbose="image")

    def test_certificate_label(self):
        """
        Test Business Description Field
        :return:
        """
        self.file_image_certificate(verbose="certificate", not_verbose="certificates")

    def test_image_method_url(self):
        """
        Test image url returned
        :return:
        """
        self.assertIn("/media/Business/Images/", self.first.image)
        self.assertNotIn("/media/Business/Certificate/", self.first.image)

    def test_certificate_method_url(self):
        """
        Test image url returned
        :return:
        """
        self.assertIn("/media/Business/Certificate/", self.first.cert)
        self.assertNotIn("/media/Business/Images/", self.first.cert)
