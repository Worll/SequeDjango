from django.urls import path
from backend import views

urlpatterns = [
    path("", views.home, name="home"),
    path("welcome", views.welcome, name="home"),

]