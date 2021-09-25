from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


class SuperuserRequiredMixin(object):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser:
            messages.warning(
                self.request,
                ":( Sorry! You do not have permissions to view this resource ",
            )
            return redirect(reverse_lazy("home"))
        return super(SuperuserRequiredMixin, self).dispatch(*args, **kwargs)
