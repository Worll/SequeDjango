from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import sys
import spotipy
import spotipy.util as util

from django.conf import settings



def home(request):

    scope = 'user-library-read'
    username = 'worll'

    client_id=settings.SPOTIFY_CLIENT_ID
    client_secret=settings.SPOTIFY_SECRET_KEY
    redirect_uri=settings.SPOTIFY_REDIRECT_URI

    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for", username)

    return HttpResponse("Hello, Django!")

def welcome(request):



    return HttpResponse("welcome")