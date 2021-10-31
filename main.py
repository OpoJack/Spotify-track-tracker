""""
    Author: Jack Oporto
    Valencia College CTSD BAS
    CEN 4930C - Seminar in Software Development
    
    Tech stack: Spotify API, spotipy, MongoDB, PyMongo
    
    This program gathers song data from Spotify's "Today's Top Hits'
    Metadata is stored in a MongoDB Atlas database.
    
    Step 1: Connect to database
    Step 2: Create new database if doesn't exist
    Step 3: Place trackIDs into testData
    Step 4: Pull data for each track and place into database
    
    For questions please contact me
    Github: https://github.com/OpoJack
    Discord: Meko#5608
    
"""""

import spotipy  # Spotify Web API wrapper for python
from datetime import datetime
from spotipy.oauth2 import SpotifyClientCredentials  # Authenticator
from pymongo import MongoClient # Database connection
from secrets import my_spotify_client_id, my_spotify_token, db_string

# Authenticates connection using private keys
auth_manager = SpotifyClientCredentials(client_id=my_spotify_client_id,
                                        client_secret=my_spotify_token)
# Access Spotify data through sp
sp = spotipy.Spotify(auth_manager=auth_manager)


# Create a connection using MongoClient.
#IMPORTANT
def get_database():
    client = MongoClient(db_string)
    return client['trackdb']


# Returns ALL track data
# IMPORTANT
def get_all_track_data(track_id, count):
    track = sp.track(track_id)
    track['Playlist Position'] = count
    track['DATE RECORDED'] = f"{datetime.today().replace(microsecond=0)}"
    return track


# Returns list of trackIDs in a given playlist
# IMPORTANT
def get_playlist_tracks(playlist_id):
    idList = []
    playlist = sp.playlist(playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        idList.append(track['id'])  # THIS GETS SPECIFIC INFO FROM EACH TRACK. 'id', 'name','popularity'
    return idList


# Returns basic data about a given trackID
# Currently unused
def get_partial_track_data(id):
    track_info = sp.track(id)

    # Track info
    track_id = track_info['id']
    name = track_info['name']
    album = track_info['album']['name']
    artist = track_info['album']['artists'][0]['name']
    release_date = track_info['album']['release_date']
    length = track_info['duration_ms']
    popularity = track_info['popularity']

    track_data = {f"Track id: {track_id}": [track_id],
                  f"Name: {name}": [name],
                  f"Album: {album}": [album],
                  f"Artist: {artist}": [artist],
                  f"Release Date: {release_date}": [release_date],
                  f"Length (ms): {length}": [length],
                  f"Popularity: {popularity}": [popularity]}
    return track_data


if __name__ == '__main__':
    # Step 1: Connect to database
    print("Connecting...")
    myDB = get_database()
    print("Connected\n")

    # Step 2: Create new database called [name] if "name" doesn't exist
    trackdb = myDB["trackdb"]

    # Step 3: Place trackIDs into testData
    track_ids = get_playlist_tracks('spotify:playlist:37i9dQZF1DXcBWIGoYBM5M')

    # Step 4: Pull data for each track and place into database
    # THE LOOP THAT DOES IT ALL 2: For real this time
    print("Writing...")
    for i in range(0, len(track_ids)):
        trackdb.insert_one(get_all_track_data((track_ids[i]), i+1))
    print(f"Successfully wrote to Database: {trackdb.name}.")

    # TODO
    # Automate this script to run every day or whenever Spotify Top Hits updates

# spotify:playlist:03R7LThwew4SbG73ypLB5s Tori tori prep
# spotify:playlist:37i9dQZF1DXcBWIGoYBM5M Top hits
