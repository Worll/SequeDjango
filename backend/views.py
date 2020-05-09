from django.shortcuts import render
from django.core import serializers

# Create your views here.
from django.http import HttpResponse
import sys
import spotipy
import spotipy.util as util

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework import viewsets
import random
import string
import json

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from spotipy.oauth2 import SpotifyClientCredentials


"""
    // TODO - use dry principle and remove repetitive code
    // TODO - add .env config template to documentation
    // TODO - raise isiues about not detaileed add track method in spotipy api
"""
class UserInfo(APIView):
    permission_classes = (IsAuthenticated,)

    """
    View to list all users in the system.

    // TODO - add authorization/authentication

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        """
        API endpoint that allows users to be viewed or edited.
        """
        username = request.user.username
        user = User.objects.get(username=username)
        return Response(user)

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        """
        API endpoint that allows users to be viewed or edited.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class ListUsers(APIView):
    """
    View to list all users in the system.

    // TODO - add authorization/authentication

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        """
        API endpoint that allows users to be viewed or edited.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        """
        API endpoint that allows users to be viewed or edited.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class PlaylistView(APIView):
    """
    View to modify playlists.

    // TODO - add authorization/authentication

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, playlist_id, format=None):
        """
        Return a list of all playlists.

        // TODO - delete this function, it's only for testing purposes and should not be allowed for users
        """
        """
        API endpoint that allows users to get all playlist.
        """
        
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        playlists = spotify.user_playlists(settings.SPOTIFY_USERNAME)

        return Response(playlists)


    def post(self, request, playlist_id, format=None):
        """
        Create and return newl playlist's url.
        """
        """
        API endpoint that allows users to create new playlists.
        """
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        playlist = sp.user_playlist_create(settings.SPOTIFY_USERNAME, "test")
        playlistURL = playlist['external_urls']['spotify']
        playlistURL_DIC = {'playlistURL': playlistURL }
        
        return Response(playlistURL_DIC)            

    def put(self, request, playlist_id, format=None):
        uris= ["1lKBe4bDNB61QkvZjPBYxJ"]
        token = util.prompt_for_user_token(settings.SPOTIFY_USERNAME, settings.SCOPE, settings.SPOTIFY_CLIENT_ID, settings.SPOTIFY_SECRET_KEY, settings.SPOTIFY_REDIRECT_URI)

        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            results = sp.user_playlist_add_tracks(settings.SPOTIFY_USERNAME, playlist_id, uris)
            return Response(results, status=200)
        else:
            return Response(status=403)            

class TrackView(APIView):
    """
    View to add new songs to queue.

    // TODO - add authorization/authentication

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Gets tracks by name.

        // TODO - delete this function, it's only for testing purposes and should not be allowed for users
        """
        """
        API endpoint that allows users to get all playlist.
        """
        
        return HttpResponse("welcome")


    def post(self, request, format=None):
        """
        Create and return newl playlist's url.
        """
        """
        API endpoint that allows users to create new playlists.
        """

        return HttpResponse("welcome")


def home(request):
    return HttpResponse("Hello, Django!")

def welcome(request):
    return HttpResponse("welcome")