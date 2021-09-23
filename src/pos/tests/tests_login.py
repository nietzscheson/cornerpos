import time

from urllib.parse import urlparse
from django.urls import reverse

from ._base import BaseTestCase


class LoginTest(BaseTestCase):
    fixtures = ["users"]

    def test_login(self):
        """
        As a user with valid credentials, I should gain
        access to the POS App.
        """
        self.selenium.get("%s%s" % (self.live_server_url, reverse("login")))
        time.sleep(1)
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("ana")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("password1234")
        time.sleep(3)
        self.selenium.find_element_by_xpath('//button[text()="Log In"]').click()

        path = urlparse(self.selenium.current_url).path
        self.assertEqual(reverse("home"), path)

        main_text = self.selenium.find_element_by_id("greeter").text
        self.assertIn("Hi ana!", main_text)
        time.sleep(3)


    def test_login_failed(self):
        """
        As a user without credentials, I should trying
        access to the POS App.
        """
        self.selenium.get("%s%s" % (self.live_server_url, reverse("login")))
        time.sleep(1)
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("pedro")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("password1234")
        time.sleep(3)
        self.selenium.find_element_by_xpath('//button[text()="Log In"]').click()

        path = urlparse(self.selenium.current_url).path
        self.assertEqual(reverse("login"), path)

        warning_text = self.selenium.find_element_by_class_name("errorlist").text
        self.assertIn("Please enter a correct username and password. Note that both fields may be case-sensitive.", warning_text)
        time.sleep(3)