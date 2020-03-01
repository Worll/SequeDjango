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

"""
    // TODO - use dry principle and remove repetitive code
    // TODO - add .env config template to documentation
"""

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
    View to list all users in the system.

    // TODO - add authorization/authentication

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all playlists.

        // TODO - delete this function, it's only for testing purposes and should not be allowed for users
        """
        """
        API endpoint that allows users to get all playlist.
        """

        token = util.prompt_for_user_token(settings.SPOTIFY_USERNAME, settings.SCOPE, settings.SPOTIFY_CLIENT_ID, settings.SPOTIFY_SECRET_KEY, settings.SPOTIFY_REDIRECT_URI)

        if token:
            sp = spotipy.Spotify(auth=token)

            playlists = sp.user_playlists(settings.SPOTIFY_USERNAME)
            return Response(playlists)

        else:
            message = "Problem with authorization flow to spotify api"
            messageJSON = serializers.serialize('json', message)
            return Response(data=messageJSON, status=403)
        return HttpResponse("welcome")


    def post(self, request, format=None):
        """
        Return newly created playlist url.
        """
        """
        API endpoint that allows users to create new playlists.
        """

        token = util.prompt_for_user_token(settings.SPOTIFY_USERNAME, settings.SCOPE, settings.SPOTIFY_CLIENT_ID, settings.SPOTIFY_SECRET_KEY, settings.SPOTIFY_REDIRECT_URI)

        if token:
            sp = spotipy.Spotify(auth=token)
            playlistURL = sp.user_playlist_create(settings.SPOTIFY_USERNAME, "test")
            return Response(playlistURL['external_urls']['spotify'])            
        else:
            return Response(status=403)
        return HttpResponse("welcome")


def home(request):
    return HttpResponse("Hello, Django!")

def welcome(request):
    return HttpResponse("welcome")