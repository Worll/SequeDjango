from django.urls import path
from backend import views

urlpatterns = [
    path("users", views.ListUsers.as_view(), name="users"),
    path("", views.home, name="home"),
    path("welcome", views.welcome, name="welcome"),
    path("playlists", views.PlaylistView.as_view(), name="playlists"),

]