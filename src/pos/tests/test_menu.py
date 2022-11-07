import time
from datetime import datetime, date, timedelta

from urllib.parse import urlparse
from seleniumlogin import force_login
from selenium.webdriver.common.by import By
from django.contrib.auth import get_user_model
from django.urls import reverse

from pos.tests._base import BaseTestCase

def test_menu_create(selenium, live_server, loaddata):
    """
    As a user with valid credentials, I should gain
    access to create a menu.
    """
    loaddata({"users"})
    user = get_user_model().objects.filter(username="ana").first()
    force_login(user, selenium, live_server)
    selenium.get("%s%s" % (live_server, reverse("pos:create")))

    option_1_input = selenium.find_element(By.NAME, "option_1")
    option_1_input.send_keys("Southern Pimento Cheese")
    option_2_input = selenium.find_element(By.NAME, "option_2")
    option_2_input.send_keys("Best-Ever Texas Caviar")
    option_3_input = selenium.find_element(By.NAME, "option_3")
    option_3_input.send_keys("Deep-Fried Peanuts")
    option_4_input = selenium.find_element(By.NAME, "option_4")
    option_4_input.send_keys("Easy Broccoli Bacon Salad")
    date_at_input = selenium.find_element(By.NAME, "date_at")
    date_at = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    date_at_input.send_keys(date_at)

    selenium.find_element(By.XPATH, '//input[@value="Save Menu"]').click()
    path = urlparse(selenium.current_url).path
    assert reverse("pos:index") == path

    success_text = selenium.find_element(By.CLASS_NAME, "success").text
    assert "Menu was created successfully" in success_text

    info_text = selenium.find_element(By.CLASS_NAME,"info").text
    assert "A notification has been sent to all users" in info_text


def test_menu_wrong_create(selenium, live_server, loaddata):
    """
    As a user with valid credentials, I should gain
    access to create a wrong menu.
    """
    loaddata({"users"})

    user = get_user_model().objects.filter(username="ana").first()
    force_login(user, selenium, live_server)
    selenium.get("%s%s" % (live_server, reverse("pos:create")))

    option_1_input = selenium.find_element(By.NAME, "option_1")
    option_1_input.send_keys("Southern Pimento Cheese")
    option_2_input = selenium.find_element(By.NAME, "option_2")
    option_2_input.send_keys("Best-Ever Texas Caviar")
    option_3_input = selenium.find_element(By.NAME, "option_3")
    option_3_input.send_keys("Deep-Fried Peanuts")
    option_4_input = selenium.find_element(By.NAME, "option_4")
    option_4_input.send_keys("Easy Broccoli Bacon Salad")
    date_at_input = selenium.find_element(By.NAME, "date_at")
    date_at = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
    date_at_input.send_keys(date_at)

    selenium.find_element(By.XPATH, '//input[@value="Save Menu"]').click()

    error_list = selenium.find_element(By.CLASS_NAME, "errorlist")
    errors_list = error_list.find_elements(By.TAG_NAME,"li")

    assert "The menu date must be equal to or greater than today" in errors_list[0].text

