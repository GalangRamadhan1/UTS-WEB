from django.urls import path
from . import views
from . import templates


urlpatterns = [
    path("members/", views.members, name="members"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("user/", views.user, name="user"),
    path("order/", views.order, name="order"),
]
