import spotify_extractor.listings_adapter as adapter
from prefect import task

@task
def get_playlist_tracks(playlist_id):
    return adapter.get_playlist_tracks(playlist_id)
