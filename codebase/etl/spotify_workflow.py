import spotify_extractor.listings_adapter as adapter
from prefect import task, flow

@task
def get_playlist_tracks(playlist_id):
    return adapter.get_playlist_tracks(playlist_id)

@task
def extract_tracks_info(tracks, playlist_id):
    return adapter.extract_tracks_info(tracks, playlist_id)

@task
def write_to_csv(tracks):
    return adapter.write_to_csv(tracks)

@flow
def extract_and_write():
    playlist_id = "37i9dQZEVXbLRQDuF5jeBp"
    playlist_tracks = get_playlist_tracks(playlist_id)
    # fill in remainder of flow here
    selected_tracks = extract_tracks_info(playlist_tracks, playlist_id)
    write_to_csv(selected_tracks)

extract_and_write()