
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
    
### How to use:
    
    Create 'secrets.py' in main folder
```python
         my_spotify_client_id = 'YOURCLIENTID'
         my_spotify_token = 'YOURTOKEN'
         db_string = 'mongodb+srv://USER:PASSWORD@DATABASE'
  ```
         
     Replace above with your own credentials for the Spotify API and MongoDB info
     run main.py

    
### Data entry example:

```yaml
{
  "_id": {
    "$oid": "61626e976753d4336bcd8e70"
  },
  "album": {
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
    "name": "Shivers"
  },
  "duration_ms": 207853,
  "id": "6bQfNiqyCX7UaQSvVVGo4I",
  "name": "Shivers",
  "popularity": 78,
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
   - `"duration_ms": 207853`
      Song length in milliseconds
      
   - `"id": "6bQfNiqyCX7UaQSvVVGo4I",`
      Isolated track ID
      
   - `"name": "Shivers",`
       Track name
   - `"popularity": 78,`
      Spotify's internal popularity rating. 1-100
   - `"uri": "spotify:track:6bQfNiqyCX7UaQSvVVGo4I",`
      Link to open track in Spotify app
   - `"Playlist Position": 1,`
      Position in Top 50 playlist. 1 = top, 50 = bottom
   - `"DATE RECORDED": "2021-10-10 00:39:51"`
      Date this specific entry was recorded
