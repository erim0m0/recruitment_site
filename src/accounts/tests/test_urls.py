from django.test import SimpleTestCase
from django.urls import resolve, reverse

from accounts.api import authentication, user_profile


class UrlsTest(SimpleTestCase):
    def test_app_name(self):
        self.assertEqual(resolve("account/api").app_name, "account:api")

