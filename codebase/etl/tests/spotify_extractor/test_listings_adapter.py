from spotify_extractor.listings_adapter import extract_tracks_info
from tests.spotify_extractor.data import tracks

def test_extract_tracks():
    playlist_id = "37i9dQZEVXbLRQDuF5jeBp"
    selected_tracks = extract_tracks_info(tracks, playlist_id)
    assert selected_tracks == [{'track_id': '3IX0yuEVvDbnqUwMBB3ouC', 'ranking': 1,
                                 'date': '2023-09-11', 
                                 'playlist_id': '37i9dQZEVXbLRQDuF5jeBp'}
                                ]