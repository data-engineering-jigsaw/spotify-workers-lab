from spotify_extractor.listings_adapter import *

playlist_id = "37i9dQZEVXbLRQDuF5jeBp"
playlist_tracks = get_playlist_tracks(playlist_id)
# selected_tracks = extract_tracks_info(playlist_tracks, playlist_id)
# write_to_csv(tracks)