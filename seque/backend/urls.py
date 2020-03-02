from django.urls import path, re_path
from backend import views

urlpatterns = [
    path("users", views.ListUsers.as_view(), name="users"),
    path("", views.home, name="home"),
    path("welcome", views.welcome, name="welcome"),
    re_path(r'^playlists(\/)?$', views.PlaylistView.as_view(), name="playlists"),
    path("playlists/<str:playlist_id>", views.PlaylistView.as_view(), name="playlists"),

]