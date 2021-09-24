import time
from datetime import datetime, date, timedelta

from urllib.parse import urlparse
from django.contrib.auth import get_user_model
from django.urls import reverse
from seleniumlogin import force_login


from ._base import BaseTestCase


class MenuTest(BaseTestCase):
    fixtures = ["users"]

    def test_menu_create(self):
        """
        As a user with valid credentials, I should gain
        access to create a menu.
        """
        user = get_user_model().objects.filter(username="ana").first()
        force_login(user, self.selenium, self.live_server_url)
        self.selenium.get("%s%s" % (self.live_server_url, reverse("pos:create")))
        time.sleep(1)
        option_1_input = self.selenium.find_element_by_name("option_1")
        option_1_input.send_keys("Southern Pimento Cheese")
        option_2_input = self.selenium.find_element_by_name("option_2")
        option_2_input.send_keys("Best-Ever Texas Caviar")
        option_3_input = self.selenium.find_element_by_name("option_3")
        option_3_input.send_keys("Deep-Fried Peanuts")
        option_4_input = self.selenium.find_element_by_name("option_4")
        option_4_input.send_keys("Easy Broccoli Bacon Salad")
        date_at_input = self.selenium.find_element_by_name("date_at")
        date_at = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        date_at_input.send_keys(date_at)

        time.sleep(3)
        self.selenium.find_element_by_xpath('//input[@value="Save Menu"]').click()
        path = urlparse(self.selenium.current_url).path
        self.assertEqual(reverse("pos:index"), path)

        success_text = self.selenium.find_element_by_class_name("success").text
        self.assertIn("Menu was created successfully", success_text)

        info_text = self.selenium.find_element_by_class_name("info").text
        self.assertIn("A notification has been sent to all users", info_text)
        time.sleep(3)
