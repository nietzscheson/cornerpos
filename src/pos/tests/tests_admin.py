from urllib.parse import urlparse
from django.urls import reverse
from selenium.webdriver.common.by import By
from pos.tests._base import BaseTestCase


class AdminTest(BaseTestCase):
    fixtures = ["users"]

    def test_login(self):
        """
        As a superuser with valid credentials, I should gain
        access to the Django admin.
        """
        self.selenium.get("%s%s" % (self.live_server_url, reverse("admin:index")))
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("ana")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("password1234")
        self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()

        path = urlparse(self.selenium.current_url).path
        self.assertEqual(reverse("admin:index"), path)

        body_text = self.selenium.find_element(By.TAG_NAME, "body").text
        self.assertIn("WELCOME, ANA.", body_text)
