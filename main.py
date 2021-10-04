# Author: Jack Oporto
# Valencia College CTSD BAS
# CEN 4930C - Seminar in Software Development
#
# Tech stack: Spotify API, spotipy, MongoDB, PyMongo
#
# This program monitors a list of songs and monitors their statistics, storing them in a database

import spotipy  # Spotify Web API wrapper for python
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth  # Auth
from spotipy.oauth2 import SpotifyClientCredentials  # Auth
import pandas as pd
import time

import pymongo
from secrets import my_spotify_client_id, my_spotify_token

auth_manager = SpotifyClientCredentials(client_id=my_spotify_client_id,
                                        client_secret=my_spotify_token)
sp = spotipy.Spotify(auth_manager=auth_manager)


# Returns artist info
def get_artist(artist_info):
    artist = sp.artist(artist_info)
    return artist


# Returns list of trackIDs in a given playlist
# IMPORTANT
def get_playlist_tracks(playlist_id):
    idList = []
    playlist = sp.playlist(playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        idList.append(track['popularity'])  # THIS GETS SPECIFIC INFO FROM EACH TRACK. 'id', 'name','popularity'
    return idList


# Simple time conversion from milliseconds to minutes
def convert_time(millis):
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)

    return f'{minutes}:{seconds}'


# Returns basic data about a given trackID
def get_track_data(id):
    track_info = sp.track(id)

# Track info
    name = track_info['name']
    album = track_info['album']['name']
    artist = track_info['album']['artists'][0]['name']
    release_date = track_info['album']['release_date']
    length = track_info['duration_ms']
    popularity = track_info['popularity']

    track_data = [name, album, artist, release_date, convert_time(length), popularity]
    return track_data

# Place data into database
    def db_insert():

        return


if __name__ == '__main__':
    print(get_artist('spotify:artist:5K4W6rqBFWDnAN6FQUkS6x'))
    print(get_track_data('spotify:track:2pX4FpOgwItRVPPUFdRcxA'))
    print(get_playlist_tracks('spotify:playlist:03R7LThwew4SbG73ypLB5s'))

# spotify:playlist:03R7LThwew4SbG73ypLB5s Tori tori prep
# spotify:playlist:37i9dQZF1DXcBWIGoYBM5M Top hits

