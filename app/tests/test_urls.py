from django.test import TestCase
from django.urls import resolve, reverse


def url_vars(self, path, view_name, route, namespace="app", kwargs=None):
    """
    :param self:
    :param path:
    :param view_name:
    :param route:
    :param namespace:
    :param kwargs:
    :return: None
    """
    if kwargs is None:
        kwargs = {}
    resolved = resolve(reverse(path, kwargs=kwargs))
    self.assertEquals(resolved.namespace, namespace)
    self.assertEquals(resolved.app_name, namespace)
    self.assertEquals(resolved.kwargs, kwargs)
    self.assertEquals(resolved.route, route)
    self.assertEqual(resolved.view_name, view_name)
    self.assertIn("api/v1/", route)


class BusinessUrlTestsCase(TestCase):
    """
    Tests for all urls related to Business Model/Api
    """
    def setUp(self) -> None:
        self.route_add = "app:add-business"
        self.route_update = "app:update-business"
        self.route_delete = "app:delete-business"
        self.kwargs = {"name": "name"}

    def test_business_read_url(self):
        """
        Correct url for reading and posting of a Business data
        :return: None
        """
        url_vars(self, path=self.route_add, view_name=self.route_add, route="api/v1/business")

    def test_business_update_url(self):
        """
        Correct url for Updating a Business Profile
        :return: None
        """
        url_vars(self, path=self.route_update, view_name=self.route_update, kwargs=self.kwargs,
                 route="api/v1/business/update/<str:name>")

    def test_business_delete_url(self):
        """
        Correct urls for deleting a Business Profile
        :return: None
        """
        url_vars(self, path=self.route_delete, view_name=self.route_delete, kwargs=self.kwargs,
                 route="api/v1/business/delete/<str:name>")


class LenderUrlTestsCase(TestCase):
    """
    Tests for all urls related to Lender Model/Api
    """
    def setUp(self) -> None:
        self.route_add = "app:add-lender"
        self.route_update = "app:update-lender"
        self.route_delete = "app:delete-lender"
        self.kwargs = {"name": "name"}

    def test_lender_read_url(self):
        """
        Correct url for reading and posting a Lender
        :return: None
        """
        url_vars(self, path=self.route_add, view_name=self.route_add, route="api/v1/lender")

    def test_lender_update_url(self):
        """
        correct url for Updating Lenders profile
        :return: None
        """
        url_vars(self, path=self.route_update, view_name=self.route_update, kwargs=self.kwargs,
                 route="api/v1/lender/update/<str:name>")

    def test_lender_delete_url(self):
        """
        Correct url for deleting a Lender
        :return: None
        """
        url_vars(self, path=self.route_delete, view_name=self.route_delete, kwargs=self.kwargs,
                 route="api/v1/lender/delete/<str:name>")


class LoanUrlTestsCase(TestCase):
    """
    Tests for all urls related to Loan Model/Api
    """
    def setUp(self) -> None:
        self.route_add = "app:add-loan"
        self.route_update = "app:update-loan"
        self.route_delete = "app:delete-loan"
        self.kwargs = {"customer": "name"}

    def test_loan_read_url(self):
        """
        correct url for reading an posting a loan request
        :return: None
        """
        url_vars(self, path=self.route_add, view_name=self.route_add, route="api/v1/loan")

    def test_loan_update_url(self):
        """
        Correct url for updating a loan request
        :return: None
        """
        url_vars(self, path=self.route_update, view_name=self.route_update, kwargs=self.kwargs,
                 route="api/v1/loan/update/<str:customer>")

    def test_loan_delete_url(self):
        """
        Correct url form deleting a Loan reuest
        :return: None
        """
        url_vars(self, path=self.route_delete, view_name=self.route_delete, kwargs=self.kwargs,
                 route="api/v1/loan/delete/<str:customer>")
