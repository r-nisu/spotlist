# 1. IMPORT LIBRARIES
# - Import spotipy to interact with Spotify API
# - Import SpotifyOAuth from spotipy.oauth2 for authentication

# 2. FUNCTION: authenticate_spotify()
def authenticate_spotify():
    # # Ask user for Spotify Client ID, Client Secret, and Redirect URI
    # # These are required for OAuth authentication (you can use your credentials)
    
    # # Set the necessary scopes for the app (e.g., playlist-modify-public, user-library-read)
    
    # # Create a SpotifyOAuth object using the user-provided credentials and scopes
    
    # # Authenticate and get an access token (with token_info from the OAuth process)
    
    # # Use the access token to create the Spotipy client object that will interact with Spotify
    
    # # Return the Spotipy client object (sp) for further operations

# 3. FUNCTION: get_liked_songs(sp)
def get_liked_songs(sp):
    # # Create an empty list to store the liked songs
    
    # # Use sp (Spotify client) to get all the saved tracks using current_user_saved_tracks() method
    
    # # Loop through the results and extract each song's details (e.g., track URI)
    # # Add each song's URI or identifier to the list
    
    # # Return the list of liked songs

# 4. FUNCTION: create_playlist(sp, playlist_name)
def create_playlist(sp, playlist_name):
    # # Get the user's Spotify ID using sp.current_user()['id']
    
    # # Call user_playlist_create() to create a new playlist with the specified name
    
    # # You can make the playlist public or private depending on your needs
    
    # # Return the playlist ID to be used later for adding songs to it

# 5. FUNCTION: add_songs_to_playlist(sp, playlist_id, liked_songs)
def add_songs_to_playlist(sp, playlist_id, liked_songs):
    # # Add each song from the liked_songs list to the new playlist using playlist_add_items()
    
    # # Pass in the playlist ID and song URIs or IDs to add the songs
    
    # # Ensure the songs are added in the correct format (Spotify API takes song URIs)

# 6. END