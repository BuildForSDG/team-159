import unittest
from django.urls import resolve, reverse


class MyTestCase(unittest.TestCase):
    def test_read_url(self):
        path = reverse("accounts:details", kwargs={"pk": 1})
        self.assertEqual(resolve(path).view_name, "accounts:details")

    def test_delete_url(self):
        path = reverse("accounts:delete", kwargs={"pk": 1})
        self.assertEqual(resolve(path).view_name, "accounts:delete")

    def test_details_url(self):
        path = reverse("accounts:all")
        self.assertEqual(resolve(path).view_name, "accounts:all")

    def test_new_url(self):
        path = reverse("accounts:new")
        self.assertEqual(resolve(path).view_name, "accounts:new")

    def test_update_url(self):
        path = reverse("accounts:update", kwargs={"pk": 1})
        self.assertEqual(resolve(path).view_name, "accounts:update")
