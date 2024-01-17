from sqlalchemy import text

from db import engine
from etl.spotify_extractor.listings_adapter import *

playlist_id = "37i9dQZEVXbLRQDuF5jeBp"
playlist_tracks = get_playlist_tracks(playlist_id)
tracks = extract_tracks_info(playlist_tracks, playlist_id)
tracks_df = pd.DataFrame(tracks)
# engine.connect().execute(text(query))
# load_to_postgres(tracks_df, engine)
# write_to_csv(tracks)