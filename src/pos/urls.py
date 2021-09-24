from django.urls import path, re_path

from . import views

app_name = "pos"

urlpatterns = [
    path("menus/", views.IndexView.as_view(), name="index"),
    path("menus/create/", views.CreateView.as_view(), name="create"),
    re_path(r"^menus/(?P<pk>[\w-]+)/$", views.DetailView.as_view(), name="detail"),
    # path('menus/(?P<pk>[\w-]+)/$/delete', views.DeleteView.as_view(), name='delete')
]
