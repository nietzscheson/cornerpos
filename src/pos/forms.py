from django.forms import ModelForm
from pos.models import Menu, Order


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ["option_1", "option_2", "option_3", "option_4", "date_at"]


class OrderForm(ModelForm):
    """The form for employees to fill their
    preferred day's meal"""

    class Meta:
        model = Order
        fields = "__all__"
        exclude = {"user", "menu"}
        labels = {
            "user": "the user",
            "option": "Choose your preferred meal",
            "preference": "Any custom preference?",
        }
