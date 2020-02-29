from django.shortcuts import render

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
        
        scope = 'playlist-modify-public'
        username = 'worll'

        client_id=settings.SPOTIFY_CLIENT_ID
        client_secret=settings.SPOTIFY_SECRET_KEY
        redirect_uri=settings.SPOTIFY_REDIRECT_URI
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

        if token:
            sp = spotipy.Spotify(auth=token)

            playlists = sp.user_playlists(username)
            return Response(playlists)

        else:
            message = "Problem with authorization flow to spotify api"
            return Response(message)
        return HttpResponse("welcome")


    def post(self, request, format=None):
        """
        Return newly created playlist url.
        """
        """
        API endpoint that allows users to create new playlists.
        """
        scope = 'playlist-modify-public'
        username = 'worll'

        client_id=settings.SPOTIFY_CLIENT_ID
        client_secret=settings.SPOTIFY_SECRET_KEY
        redirect_uri=settings.SPOTIFY_REDIRECT_URI
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

        if token:
            sp = spotipy.Spotify(auth=token)
            playlistURL = sp.user_playlist_create(username, "test")
            return Response(playlistURL['external_urls']['spotify'])            
        else:
            message = "Problem with authorization flow to spotify api"
            return Response(message)
        return HttpResponse("welcome")


def home(request):
    return HttpResponse("Hello, Django!")

def playlists(request):

    scope = 'playlist-modify-public'
    username = 'worll'

    client_id=settings.SPOTIFY_CLIENT_ID
    client_secret=settings.SPOTIFY_SECRET_KEY
    redirect_uri=settings.SPOTIFY_REDIRECT_URI
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print()
                print(playlist['name'])
                print ('  total tracks', playlist['tracks']['total'])
                results = sp.playlist(playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                while tracks['next']:
                    tracks = sp.next(tracks)
    else:
        print("Can't get token for", username)

def welcome(request):
    return HttpResponse("welcome")

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))