
# Spotify-track-tracker

### Description:  

    This program gathers song data from Spotify's playlist "Today's Top Hits'
    each time it's updated
    Metadata is stored in a MongoDB Atlas database.
    
    Program steps:
    Step 1: Connect to database
    Step 2: Create new database if doesn't exist
    Step 3: Place trackIDs into testData
    Step 4: Pull data for each track and place into database

### Tech stack: 

    Spotify API, spotipy, MongoDB, PyMongo
    
### Data entry example:

```yaml
{
  "_id": {
    "$oid": "61626e976753d4336bcd8e70"
  },
  "album": {
    "album_type": "single",
    "artists": [
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/6eUKZXaKkcviH0Ku9w2n3V"
        },
        "href": "https://api.spotify.com/v1/artists/6eUKZXaKkcviH0Ku9w2n3V",
        "id": "6eUKZXaKkcviH0Ku9w2n3V",
        "name": "Ed Sheeran",
        "type": "artist",
        "uri": "spotify:artist:6eUKZXaKkcviH0Ku9w2n3V"
      }
    ],
    "external_urls": {
      "spotify": "https://open.spotify.com/album/5kFCfioZraFsRWpoitQjmx"
    },
    "id": "5kFCfioZraFsRWpoitQjmx",
    "images": [
      {
        "height": 640,
        "url": "https://i.scdn.co/image/ab67616d0000b273469407300636945a5eb2d9ed",
        "width": 640
      },
      {
        "height": 300,
        "url": "https://i.scdn.co/image/ab67616d00001e02469407300636945a5eb2d9ed",
        "width": 300
      },
      {
        "height": 64,
        "url": "https://i.scdn.co/image/ab67616d00004851469407300636945a5eb2d9ed",
        "width": 64
      }
    ],
    "name": "Shivers",
    "release_date": "2021-09-10",
    "total_tracks": 1
  },
  "artists": [
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/6eUKZXaKkcviH0Ku9w2n3V"
      },
      "href": "https://api.spotify.com/v1/artists/6eUKZXaKkcviH0Ku9w2n3V",
      "id": "6eUKZXaKkcviH0Ku9w2n3V",
      "name": "Ed Sheeran",
      "type": "artist",
      "uri": "spotify:artist:6eUKZXaKkcviH0Ku9w2n3V"
    }
  ],
  "duration_ms": 207853,
  "external_urls": {
    "spotify": "https://open.spotify.com/track/6bQfNiqyCX7UaQSvVVGo4I"
  },
  "id": "6bQfNiqyCX7UaQSvVVGo4I",
  "name": "Shivers",
  "popularity": 78,
  "preview_url": null,
  "track_number": 1,
  "uri": "spotify:track:6bQfNiqyCX7UaQSvVVGo4I",
  "Playlist Position": 1,
  "DATE RECORDED": "2021-10-10 00:39:51"
  }
  ```

### Data explained:

  - `"_id": {
    "$oid": "61626e976753d4336bcd8e70"}`
     oid = Object id within this database
  - `"album"`
      Contains all album info inside
    - `"album_type": "single",`
        Usually either ***'single'*** or ***'album'***
    - `"artists":`
      Contains all artist data involved in track
      
       - `"external_urls": {
            "spotify": "https://open.spotify.com/artist/6eUKZXaKkcviH0Ku9w2n3V"`
        
           URL to open this artist on Spotify Web client 
        
       - `"href": "https://api.spotify.com/v1/artists/6eUKZXaKkcviH0Ku9w2n3V",`
        
          Spotify api link to the artist
        - `"id": "6eUKZXaKkcviH0Ku9w2n3V",`
            Artist id
            
        - `"name": "Ed Sheeran",`
            Artist name

        - `"type": "artist",`
            Usually "artist"
          
        - `"uri": "spotify:artist:6eUKZXaKkcviH0Ku9w2n3V"`
            (Uniform Resource Indicator) Link to open artist in Spotify app
   - `"id": "5kFCfioZraFsRWpoitQjmx"`
       Isolated album ID
   - `"images"`
      Album artwork in three different sizes
   - `"artists"`
       Redundant data info for this track, same as "artists" above
   - `"duration_ms": 207853`
      Song length in milliseconds
   - `"external_urls": {
    "spotify": "https://open.spotify.com/track/6bQfNiqyCX7UaQSvVVGo4I"`
    
      URL to open this track on Spotify Web client
      
   - `"id": "6bQfNiqyCX7UaQSvVVGo4I",`
      Isolated track ID
      
   - `"name": "Shivers",`
       Track name
   - `"popularity": 78,`
      Spotify's internal popularity rating. 1-100
   - `"track_number": 1,`
      Track number within album
   - `"uri": "spotify:track:6bQfNiqyCX7UaQSvVVGo4I",`
      Link to open track in Spotify app
   - `"Playlist Position": 1,`
      Position in Top 50 playlist. 1 = top, 50 = bottom
   - `"DATE RECORDED": "2021-10-10 00:39:51"`
