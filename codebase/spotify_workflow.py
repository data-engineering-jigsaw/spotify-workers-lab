from prefect import flow, task
from prefect.deployments.deployments import Deployment
from prefect.server.schemas.schedules import IntervalSchedule

import etl.spotify_extractor.listings_adapter as adapter


@task
def get_playlist_tracks(playlist_id):
    return adapter.get_playlist_tracks(playlist_id)

@task
def extract_tracks_info(tracks, playlist_id):
    return adapter.extract_tracks_info(tracks, playlist_id)

@task
def write_to_csv(tracks):
    return adapter.write_to_csv(tracks)

@task
def load_files_to_postgres():
    return adapter.load_files_to_postgres()

@flow(name="extract_and_write")
def extract_and_write(playlist_id):    
    playlist_tracks = get_playlist_tracks(playlist_id)
    selected_tracks = extract_tracks_info(playlist_tracks, playlist_id)
    write_to_csv(selected_tracks)
    load_files_to_postgres()

if __name__ == "__main__":

    playlist_id = "37i9dQZEVXbLRQDuF5jeBp"
    # extract_and_write(playlist_id)

    schedule = IntervalSchedule(interval=10)
    parameters = {'playlist_id': playlist_id}
    deployment = Deployment.build_from_flow(
        name="new_deployment",
        flow=extract_and_write,
        version=1,
        schedule=schedule,
        is_schedule_active=True,
        work_queue_name="default",
        parameters=parameters,
        entrypoint="./spotify_workflow.py:extract_and_write",
    )
    deployment.apply(upload=True)