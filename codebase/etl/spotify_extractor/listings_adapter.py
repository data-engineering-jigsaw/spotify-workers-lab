import os
from datetime import date

import pandas as pd
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from db import engine
from etl.spotify_extractor.spotify_client import client


def get_playlist_tracks(playlist_id):
    playlist = client.playlist_items(playlist_id)
    tracks = playlist['items']
    return tracks

def extract_tracks_info(tracks, playlist_id):
    selected_tracks = []
    current_date = str(date.today())
    for idx, track in enumerate(tracks):
        track_id = track['track']['id']
        ranking = idx + 1
        selected_track = {'track_id': track_id,
                          'ranking': ranking,
                          'date': current_date,
                          'playlist_id': playlist_id
                          }
        selected_tracks.append(selected_track)
    return selected_tracks

def write_to_csv(tracks):
    current_date = str(date.today())
    
    folder_path = "./data/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    tracks_df = pd.DataFrame(tracks)
    data_path = f"./data/{current_date}-track-listings.csv"
    tracks_df.to_csv(data_path)

def find_recent_files(engine):
    date = read_sql("select max(date) from tracks", engine).iloc[0, 0]
    text_date = str(date)
    files = os.listdir('./data')
    
    recent_files = []
    for file in files:
        file_date = file.replace('-track-listings.csv', '')
        if file_date > text_date:
            recent_files.append(file)
    
    return recent_files

def load_files_to_postgres():
    recent_files = find_recent_files(engine)
    dfs = [pd.read_csv(f'./data/{recent_file}', index_col = 0) for recent_file in recent_files]
    
    for df in dfs:
        load_to_postgres(df, engine)
        

def load_to_postgres(df, engine, table_name = 'tracks'):
    df.to_sql(table_name, engine, if_exists='append', index=False)

def read_sql(query, engine):
    df = pd.DataFrame(engine.connect().execute(text(query)))
    return df
    
    