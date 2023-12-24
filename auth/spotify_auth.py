import spotipy
from spotipy.oauth2 import SpotifyOAuth
from plyer import notification
import os
from dotenv import load_dotenv

load_dotenv()

def authenticate_spotify():
    try:
        # Set up Spotify API client with authentication and required scope
        client_id = os.getenv('SPOTIFY_CLIENT_ID')
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
        scope = 'user-read-currently-playing'
        
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
        return sp
    except spotipy.SpotifyException as e:
        # Handle Spotify API authentication errors 
        print("Spotify API authentication error:", e)
        return None

def refresh_access_token(sp):
    try:
        sp_oauth = sp.auth_manager
        if sp_oauth.is_token_expired(sp_oauth.get_access_token()):
            sp_oauth.refresh_access_token(sp_oauth.get_refresh_token())
        return sp  # Return the refreshed Spotify object
    except spotipy.SpotifyException as e:
        # Handle token refresh errors
        print("Error refreshing access token:", e)
        return None

def get_currently_playing_track(sp):
    try:
        # Retrieve the currently playing track using the Spotify API client
        track_info = sp.current_user_playing_track()
        return track_info
    except spotipy.SpotifyException as e:
        # Handle Spotify API errors when retrieving the currently playing track
        print("Error retrieving currently playing track:", e)
        return None

def send_message(track_info):
    # Extract relevant information from the track_info
    track_name = track_info['item']['name']
    artist_name = track_info['item']['artists'][0]['name']
    message_text = f"Currently listening to: {track_name} by {artist_name}"

    # Use Plyer to display a desktop notification
    notification.notify(
        title='Spotify Notification',
        message=message_text,
        app_name='Spotify Notification',
        timeout=10
    )

sp = authenticate_spotify()
if sp:
    track_info = get_currently_playing_track(sp)
    if track_info:
        send_message(track_info)


def get_spotify_auth_url(client_id, client_secret, redirect_uri, scope):
    try:
        sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
        auth_url = sp_oauth.get_authorize_url()
        return auth_url
    except Exception as e:
        print("An error occurred while getting the authorization URL:", e)
        return None

# Call the function to get the authorization URL

