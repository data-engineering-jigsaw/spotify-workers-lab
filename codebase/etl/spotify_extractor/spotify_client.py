from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from spotify_extractor.settings import CLIENT_ID, CLIENT_SECRET

def spotify_client():    
    credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret = CLIENT_SECRET)
    client = spotipy.Spotify(client_credentials_manager=credentials_manager)
    return client

client = spotify_client()


