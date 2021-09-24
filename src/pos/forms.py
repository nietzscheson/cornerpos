from django.forms import ModelForm
from pos.models import Menu


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ["option_1", "option_2", "option_3", "option_4", "date_at"]
