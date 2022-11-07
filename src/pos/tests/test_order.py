import time
from datetime import datetime, date, timedelta
from seleniumlogin import force_login
from selenium.webdriver.support.ui import Select
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from django.contrib.auth import get_user_model
from django.urls import reverse

from pos.models import Menu, Order
from pos.tests._base import BaseTestCase

def test_order_create(selenium, live_server, loaddata):
    """
    As a user with valid credentials, I should gain
    access to create a order.
    """
    loaddata({"users", "menus"})

    menu = Menu.objects.get()

    selenium.get(
        "%s%s"
        % (live_server, reverse("pos:detail", kwargs={"pk": menu.id}))
    )

    selenium.find_element(By.XPATH, '//a[text()="Go to order"]').click()

    username_input = selenium.find_element(By.NAME, "username")
    username_input.send_keys("miguel")
    password_input = selenium.find_element(By.NAME, "password")
    password_input.send_keys("password123!")

    selenium.find_element(By.XPATH, '//button[text()="Log In"]').click()

    order_path = urlparse(selenium.current_url).path
    assert reverse("pos:order-create", kwargs={"menu_id": menu.id}) == order_path

    title = selenium.find_element(By.ID, "title").text
    assert "Create Order" in title

    selenium.find_element(By.XPATH, "//select[@id='id_option']/option[text()='Option 3']").click()

    custom_preference = selenium.find_element(By.NAME, "preference")
    custom_preference.send_keys("Without salt!")

    selenium.find_element(By.XPATH, '//input[@value="Save Order"]').click()

    path = urlparse(selenium.current_url).path
    assert reverse("pos:detail", kwargs={"pk": menu.id}) == path

    success_text = selenium.find_element(By.CLASS_NAME, "success").text
    assert "Order was created successfully" in success_text

    title = selenium.find_element(By.ID, "title").text
    assert "We're preparing your meal!" in title


def test_order_created(selenium, live_server, loaddata):
    """
    As a user with valid credentials, I should gain
    access to create a order.
    """
    loaddata({"users", "menus", "orders"})
    menu = Menu.objects.get()
    order = Order.objects.get()

    user = get_user_model().objects.filter(username="miguel").first()
    force_login(user, selenium, live_server)
    selenium.get(
        "%s%s"
        % (live_server, reverse("pos:detail", kwargs={"pk": menu.id}))
    )

    menu_id = selenium.find_element(By.ID, "menu_id").text
    assert str(menu.id) in menu_id

    order_id = selenium.find_element(By.ID, "order_id").text
    assert str(order.id) in order_id

    title = selenium.find_element(By.ID, "title").text
    assert "We're preparing your meal!" in title



def test_order_dont_access(selenium, live_server, loaddata):
    """
    As a user with valid credentials, I should no gain
    access to list system orders.
    """
    loaddata({"users", "menus", "orders"})

    user = get_user_model().objects.filter(username="miguel").first()
    force_login(user, selenium, live_server)
    selenium.get("%s%s" % (live_server, reverse("pos:index")))

    warning_text = selenium.find_element(By.CLASS_NAME, "warning").text
    assert ":( Sorry! You do not have permissions to view this resource" in warning_text

    home_path = urlparse(selenium.current_url).path
    assert reverse("home") == home_path
