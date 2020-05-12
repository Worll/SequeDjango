from django.urls import path, re_path
from backend import views

urlpatterns = [
    re_path(r'^api/user(\/)?$', views.UserInfo.as_view(), name="user_info"),
    re_path(r'^api/register(\/)?$', views.RegisterUser.as_view(),
            name="user_registration"),
    path("", views.home, name="home"),
    path("api/welcome", views.welcome, name="welcome"),
    re_path(r'^api/playlists(\/)?$',
            views.PlaylistView.as_view(), name="playlists"),
    path("playlists/<str:playlist_id>",
         views.PlaylistView.as_view(), name="playlists"),
    re_path(r'^api/room(\/)?$', views.RoomView.as_view(),
            name="room")

]
