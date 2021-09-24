import time
from datetime import datetime, date, timedelta

from urllib.parse import urlparse
from django.contrib.auth import get_user_model
from django.urls import reverse
from seleniumlogin import force_login
from selenium.webdriver.support.ui import Select
from pos.models import Menu


from ._base import BaseTestCase


class OrderTest(BaseTestCase):
    fixtures = ["users", "menus"]

    def test_order_create(self):
        """
        As a user with valid credentials, I should gain
        access to create a order.
        """
        user = get_user_model().objects.filter(username="ana").first()
        force_login(user, self.selenium, self.live_server_url)

        menu = Menu.objects.get()

        self.selenium.get("%s%s" % (self.live_server_url, reverse("pos:detail", kwargs={"pk": menu.id})))
        time.sleep(3)

        self.selenium.find_element_by_xpath('//a[text()="Go to order"]').click()

        order_path = urlparse(self.selenium.current_url).path
        self.assertEqual(reverse("pos:order-create", kwargs={"menu_id": menu.id}), order_path)

        title = self.selenium.find_element_by_id("title").text
        self.assertIn("Create Order", title)

        prefered_meal = Select(self.selenium.find_element_by_id('id_option'))
        prefered_meal.select_by_visible_text('Option 3')

        custom_preference = self.selenium.find_element_by_name("preference")
        custom_preference.send_keys("Without salt!")

        time.sleep(3)

        self.selenium.find_element_by_xpath('//input[@value="Save Order"]').click()

        path = urlparse(self.selenium.current_url).path
        self.assertEqual(reverse("pos:detail", kwargs={"pk": menu.id}), path)

        success_text = self.selenium.find_element_by_class_name("success").text
        self.assertIn("Order was created successfully", success_text)


        title = self.selenium.find_element_by_id("title").text
        self.assertIn("We're preparing your meal!", title)
