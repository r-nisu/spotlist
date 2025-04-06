from spotify_utils import authenticate_spotify, get_liked_songs, create_playlist, add_songs_to_playlist

def main():
    # 2. USER AUTHENTICATION
    # Call authenticate_spotify to authenticate the user and get the Spotify client (sp)
    sp = authenticate_spotify()
    
    # 3. GET LIKED SONGS
    # Call get_liked_songs to fetch all the liked songs from the user's account
    liked_songs = get_liked_songs(sp)
    
    # 4. ASK FOR NEW PLAYLIST NAME
    # Ask the user to input the name of the new playlist they want to create
    playlist_name = input("Enter the name of the new playlist: ")

    # 5. CREATE PLAYLIST
    # Call create_playlist to create a new playlist with the given name
    playlist_id = create_playlist(sp, playlist_name)
    
    # 6. ADD SONGS TO PLAYLIST
    # Call add_songs_to_playlist to add the liked songs to the newly created playlist
    add_songs_to_playlist(sp, playlist_id, liked_songs)
    
    # 7. CONFIRM SUCCESS
    # Print a success message once the playlist is created and songs are added
    print(f"Your new playlist '{playlist_name}' has been created and populated with your liked songs!")

# 8. RUN THE MAIN FUNCTION
# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()