import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import time

def setup_env():
    """
    Checks if the .env file exists. If not, prompts the user to create it.
    """
    if not os.path.exists(".env"):
        print(".env file missing.")
        print("Let's set it up now.")
        client_id = input("\nEnter your Spotify Client ID: ")
        client_secret = input("Enter your Spotify Client Secret: ")
        redirect_uri = input("Enter your Redirect URI (e.g., http://localhost:8888/callback): ")

        with open(".env", "w") as env_file:
            env_file.write(f"SPOTIPY_CLIENT_ID={client_id}\n")
            env_file.write(f"SPOTIPY_CLIENT_SECRET={client_secret}\n")
            env_file.write(f"SPOTIPY_REDIRECT_URI={redirect_uri}\n")

        print(".env file created successfully.")
    else:
        print(".env file found. Proceeding...")

    load_dotenv()  # Load the .env file after creation
    return os.getenv("SPOTIPY_CLIENT_ID"), os.getenv("SPOTIPY_CLIENT_SECRET"), os.getenv("SPOTIPY_REDIRECT_URI")

def authenticate_spotify():
    """
    Authenticates the user with Spotify using the credentials stored in the .env file.
    If the .env file is missing or invalid, prompts the user to set it up.
    """
    client_id, client_secret, redirect_uri = setup_env()
    scope = "playlist-modify-private user-library-read"

    sp_oauth = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        open_browser=True
        )
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    return sp

def get_liked_songs(sp):
    """
    Fetches the user's liked songs from Spotify.
    """ 
    liked_songs = []
    try:
        results = sp.current_user_saved_tracks(limit=50)  # Fetch the first page of liked songs

        while results:
            for item in results.get("items", []):
                track = item["track"]
                liked_songs.append(track["uri"])
            results = sp.next(results) if results and results.get("next") else None  

    except Exception as e:
        print(f"Error fetching liked songs: {e}")
        return []

    return liked_songs

def create_playlist(sp, playlist_name):
    """
    Creates a new playlist for the user.
    """
    user_id = sp.current_user()['id']

    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

    return playlist['id']

def add_songs_to_playlist(sp, playlist_id, liked_songs):
    """
    Adds the user's liked songs to the specified playlist.
    """
    for i in range(0, len(liked_songs), 100):
        sp.playlist_add_items(playlist_id=playlist_id, items=liked_songs[i:i+100])
        time.sleep(1)