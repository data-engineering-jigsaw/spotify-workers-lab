from spotify_extractor.spotify_client import client
from datetime import date
import pandas as pd


def get_playlist_tracks(playlist_id):
    playlist = client.playlist_items(playlist_id)
    tracks = playlist['items']
    return tracks

def extract_tracks_info(tracks, playlist_id):
    pass

def write_to_csv(tracks):
    tracks_df = pd.DataFrame(tracks)
    data_path = "./data/track_listings.csv"
    tracks_df.to_csv(data_path)


    
    