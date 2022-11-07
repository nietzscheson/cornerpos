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


class OrderCreateTest(BaseTestCase):
    fixtures = ["users", "menus"]

    def test_order_create(self):
        """
        As a user with valid credentials, I should gain
        access to create a order.
        """
        menu = Menu.objects.get()

        self.selenium.get(
            "%s%s"
            % (self.live_server_url, reverse("pos:detail", kwargs={"pk": menu.id}))
        )

        self.selenium.find_element(By.XPATH, '//a[text()="Go to order"]').click()

        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("miguel")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("password123!")

        self.selenium.find_element(By.XPATH, '//button[text()="Log In"]').click()

        order_path = urlparse(self.selenium.current_url).path
        self.assertEqual(
            reverse("pos:order-create", kwargs={"menu_id": menu.id}), order_path
        )

        title = self.selenium.find_element(By.ID, "title").text
        self.assertIn("Create Order", title)

        self.selenium.find_element(By.XPATH, "//select[@id='id_option']/option[text()='Option 3']").click()

        custom_preference = self.selenium.find_element(By.NAME, "preference")
        custom_preference.send_keys("Without salt!")

        self.selenium.find_element(By.XPATH, '//input[@value="Save Order"]').click()

        path = urlparse(self.selenium.current_url).path
        self.assertEqual(reverse("pos:detail", kwargs={"pk": menu.id}), path)

        success_text = self.selenium.find_element(By.CLASS_NAME, "success").text
        self.assertIn("Order was created successfully", success_text)

        title = self.selenium.find_element(By.ID, "title").text
        self.assertIn("We're preparing your meal!", title)


class OrderCreatedTest(BaseTestCase):
    fixtures = ["users", "menus", "orders"]

    def test_order_created(self):
        """
        As a user with valid credentials, I should gain
        access to create a order.
        """
        menu = Menu.objects.get()
        order = Order.objects.get()

        user = get_user_model().objects.filter(username="miguel").first()
        force_login(user, self.selenium, self.live_server_url)
        self.selenium.get(
            "%s%s"
            % (self.live_server_url, reverse("pos:detail", kwargs={"pk": menu.id}))
        )

        menu_id = self.selenium.find_element(By.ID, "menu_id").text
        self.assertIn(str(menu.id), menu_id)

        order_id = self.selenium.find_element(By.ID, "order_id").text
        self.assertIn(str(order.id), order_id)

        title = self.selenium.find_element(By.ID, "title").text
        self.assertIn("We're preparing your meal!", title)


class OrderDontAccessTest(BaseTestCase):
    fixtures = ["users", "menus", "orders"]

    def test_order_dont_access(self):
        """
        As a user with valid credentials, I should no gain
        access to list system orders.
        """

        user = get_user_model().objects.filter(username="miguel").first()
        force_login(user, self.selenium, self.live_server_url)
        self.selenium.get("%s%s" % (self.live_server_url, reverse("pos:index")))

        warning_text = self.selenium.find_element(By.CLASS_NAME, "warning").text
        self.assertIn(
            ":( Sorry! You do not have permissions to view this resource", warning_text
        )

        home_path = urlparse(self.selenium.current_url).path
        self.assertEqual(reverse("home"), home_path)
