from urllib.parse import urlparse
from django.urls import reverse
from selenium.webdriver.common.by import By
from pos.tests._base import BaseTestCase
import pytest


# @pytest.mark.usefixtures("users")
def test_login(selenium, live_server, loaddata):
    """
    As a superuser with valid credentials, I should gain
    access to the Django admin.
    """
    loaddata({"users"})
    selenium.get("%s%s" % (live_server.url, reverse("admin:index")))
    username_input = selenium.find_element(By.NAME, "username")
    username_input.send_keys("ana")
    password_input = selenium.find_element(By.NAME, "password")
    password_input.send_keys("password1234")
    selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()

    path = urlparse(selenium.current_url).path
    assert reverse("admin:index") == path

    body_text = selenium.find_element(By.TAG_NAME, "body").text

    assert "WELCOME, ANA." in body_text
