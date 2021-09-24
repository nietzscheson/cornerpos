from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from pos.models import Menu
from pos.forms import MenuForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from pos.task import slack_notification
from core.settings import LOGGER


class IndexView(LoginRequiredMixin, ListView):
    context_object_name = "latest_menu_list"

    def get_queryset(self):
        return Menu.objects.order_by("created_at")


class CreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Menu
    form_class = MenuForm
    success_url = reverse_lazy("pos:index")
    success_message = "Menu was created successfully"

    def post(self, request):
        response = super(CreateView, self).post(request)

        try:
            slack_notification.delay(self.object.id)
            messages.info(request, "A notification has been sent to all users")
        except Exception as error:
            messages.error(request, error)
            LOGGER.error(error)

        return response


class DetailView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Menu
    form_class = MenuForm
    success_url = reverse_lazy("pos:index")
    success_message = "Menu was updated successfully"


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Menu
    success_url = reverse_lazy("pos:index")
