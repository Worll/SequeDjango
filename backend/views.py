from django.shortcuts import render
from django.core import serializers
from django.forms.models import model_to_dict

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
import uuid

from .models import *

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from spotipy.oauth2 import SpotifyClientCredentials


class RegisterUser(APIView):

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        """
        API endpoint that allows users to be viewed or edited.
        """
        from django.contrib.auth.models import User
        user = User.objects.create_user(
            'svecias2', '', 'svecias2')
        user_obj = model_to_dict(user)
        user_obj.pop('password', None)
        return Response(user_obj)


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

        # assuming obj is your model instance
        user_obj = model_to_dict(user)
        user_obj.pop('password', None)

        return Response(user_obj)

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        """
        API endpoint that allows users to be viewed or edited.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


class SearchView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, query):
        if not query:
            return Response(status=400)

        spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials())
        results = spotify.search(q=query, type='track')

        return Response(results)


class RoomView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, room_id):
        """
        Return a list of all users.
        """
        """
        API endpoint that allows users to be viewed or edited.
        """

        user_id = request.user.id

        room = Room.objects.get(pk=room_id)

        if room.organizer != user_id:
            pass  # TODO: null not organiser fields (not organiser fields)

        return Response(model_to_dict(room))

    def post(self, request, format=None):
        """
        Create and return newl playlist's url.
        """
        """
        API endpoint that allows users to create new playlists.
        """
        token = util.prompt_for_user_token(settings.SPOTIFY_USERNAME, settings.SCOPE,
                                           settings.SPOTIPY_CLIENT_ID, settings.SPOTIPY_CLIENT_SECRET, settings.SPOTIFY_REDIRECT_URI)

        if not token:
            return Response(status=403)

        sp = spotipy.Spotify(auth=token)
        playlist = sp.user_playlist_create(
            settings.SPOTIFY_USERNAME, "test")
        playlistURL = playlist['external_urls']['spotify']

        username = request.user.username
        user = User.objects.get(username=username)
        inviteCode = '{}'.format(uuid.uuid4())[:8]
        room = Room.objects.create_instance(organizer=user,
                                            playlistUrl=playlistURL, inviteCode=inviteCode)
        return Response({"uid": room.uid})


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
