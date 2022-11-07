import time

from urllib.parse import urlparse
from django.urls import reverse
from selenium.webdriver.common.by import By


def test_login(selenium, live_server, loaddata):
    """
    As a user with valid credentials, I should gain
    access to the POS App.
    """
    loaddata({"users"})
    selenium.get("%s%s" % (live_server, reverse("login")))

    username_input = selenium.find_element(By.NAME, "username")
    username_input.send_keys("ana")
    password_input = selenium.find_element(By.NAME, "password")
    password_input.send_keys("password1234")

    selenium.find_element(By.XPATH, '//button[text()="Log In"]').click()

    path = urlparse(selenium.current_url).path
    assert reverse("home") == path

    main_text = selenium.find_element(By.ID, "greeter").text
    assert "Hi ana!" in main_text

def test_login_failed(selenium, live_server, loaddata):
    """
    As a user without credentials, I should trying
    access to the POS App.
    """
    loaddata({"users"})
    selenium.get("%s%s" % (live_server, reverse("login")))

    username_input = selenium.find_element(By.NAME, "username")
    username_input.send_keys("pedro")
    password_input = selenium.find_element(By.NAME, "password")
    password_input.send_keys("password1234")

    selenium.find_element(By.XPATH, '//button[text()="Log In"]').click()

    path = urlparse(selenium.current_url).path
    assert reverse("login") == path

    warning_text = selenium.find_element(By.CLASS_NAME, "errorlist").text
    assert "Please enter a correct username and password. Note that both fields may be case-sensitive." in warning_text
