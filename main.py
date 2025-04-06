from spotify_utils import authenticate_spotify, get_liked_songs, create_playlist, add_songs_to_playlist
import time

def main():
    print("Welcome to Spotlist!")
    print("This program will create a playlist from your liked songs on Spotify.\n")
    print("Make sure you have your Spotify Developer credentials ready.")
    print("If you don't have them, visit https://developer.spotify.com/dashboard/ to create an app.\n")
    time.sleep(5)

    sp = authenticate_spotify()
    print("Authentication successful!\n")
    time.sleep(2)

    liked_songs = get_liked_songs(sp)
    if not liked_songs:
        print("No liked songs found in your Spotify account.")
        time.sleep(2)
        return
    
    playlist_name = input("Enter the name of the new playlist: ")
    playlist_id = create_playlist(sp, playlist_name)
    print(f"'{playlist_name}' created successfully.\n")
    time.sleep(3)
     
    add_songs_to_playlist(sp, playlist_id, liked_songs)
    print(f"Liked songs have been added to '{playlist_name}'.")
    time.sleep(3)

if __name__ == "__main__":
    main()