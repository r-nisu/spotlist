# Spotlist

Spotlist is a Python script that connects to your Spotify account, retrieves your liked songs, and creates a new playlist with them. This tool simplifies the process of organizing your favorite tracks into a playlist.

---

## Features

- Authenticate with your Spotify account via browser login.
- Retrieve all your liked songs from Spotify.
- Automatically create a new playlist with your liked songs.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- A Spotify Developer account ([create one here](https://developer.spotify.com/dashboard/))

### Steps

1. Clone or download the project:

   ```bash
   git clone https://github.com/yourusername/spotlist.git
   cd spotlist
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a Spotify Developer App:

   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Create an app and get your `Client ID` and `Client Secret`.
   - Add a Redirect URI: `http://127.0.0.1:8888/callback`.

4. Run the script:
   ```bash
   python main.py
   ```

---

## Configuration

If the `.env` file is missing, the program will prompt you to enter your Spotify credentials (Client ID, Client Secret, and Redirect URI) during the first run. Alternatively, you can manually create a `.env` file in the project directory with the following content:

```
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
```

Replace `your_client_id` and `your_client_secret` with the credentials from your Spotify Developer App.

---

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. Follow the prompts:

   - Log in to your Spotify account when the browser opens.
   - Enter a name for the new playlist.
   - The script will fetch your liked songs and add them to the new playlist.

3. Open Spotify and enjoy your new playlist.

---

## Troubleshooting

### Common Issues

1. **`ModuleNotFoundError: No module named 'dotenv'`**

   - Ensure you have installed the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **`Fatal error in launcher: Unable to create process using`**

   - Ensure Python is installed correctly and added to your system's PATH.
   - Reinstall Python if necessary.

3. **Redirect URI Warning**

   - Use `http://127.0.0.1:8888/callback` as the Redirect URI in both your `.env` file and Spotify Developer App.

4. **No Liked Songs Found**
   - Ensure you have liked songs in your Spotify account.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Built using [Spotipy](https://spotipy.readthedocs.io/) and [python-dotenv](https://pypi.org/project/python-dotenv/).
- Inspired by the need to organize liked songs into playlists effortlessly.

---
