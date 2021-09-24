from django.urls import path, re_path

from . import views

app_name = "pos"

urlpatterns = [
    path("menus/", views.IndexView.as_view(), name="index"),
    path("menus/create/", views.CreateView.as_view(), name="create"),
    re_path(r"^menus/(?P<pk>[\w-]+)/$", views.UpdateView.as_view(), name="update"),
    re_path(
        r"^menus/detail/(?P<pk>[\w-]+)/$", views.DetailView.as_view(), name="detail"
    ),
    re_path(
        r"^orders/create/(?P<menu_id>[\w-]+)/$",
        views.OrderCreateView.as_view(),
        name="order-create",
    ),
]
