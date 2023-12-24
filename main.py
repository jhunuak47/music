import random
from auth.spotify_auth import authenticate_spotify, get_currently_playing_track, refresh_access_token,send_message
from messaging.message_service import send_message
from auth.spotify_auth import get_spotify_auth_url
from dotenv import load_dotenv
import os

def generate_message(song, girlfriend_name):
    messages = [
        f"Hey {girlfriend_name}, I noticed you're listening to {song}. It's one of my favorites too!",
        f"Thinking of you while you enjoy {song}. Hope you're having a great time, {girlfriend_name}!",
        f"Your taste in music is as wonderful as you are, {girlfriend_name}. Enjoying {song} right now?",
        f"Just wanted to say that {song} is a fantastic choice! It always puts me in a good mood, {girlfriend_name}.",
        f"Listening to {song} always reminds me of our special moments together, {girlfriend_name}. Sending you lots of love!",
        f"Can't help but smile knowing you're enjoying {song}, {girlfriend_name}. Your music brightens my day too!",
        f"{song} is such a timeless classic, {girlfriend_name}. It's like the soundtrack to our love story.",
        f"Your music taste is impeccable, just like you, {girlfriend_name}. Enjoy every note of {song}!",
        f"Every time I hear {song}, it brings back memories of us. Thanks for sharing your music with me, {girlfriend_name}!",
    ]
    return random.choice(messages)

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
    scope = 'user-read-currently-playing'
    
    auth_url = get_spotify_auth_url(client_id, client_secret, redirect_uri, scope)
    print(auth_url)

def main():
    sp = authenticate_spotify()

    if sp:
        print("Authentication successful!")
        currently_playing = get_currently_playing_track(sp)
        if currently_playing is not None:
            song = currently_playing['item']['name']
            girlfriend_name = "Khushi"
            message = generate_message(song, girlfriend_name)
            recipient_email = "kulwanti1201@gmail.com" 
            send_message(recipient_email, "love You", message)

        # Call the refresh_access_token function
        sp = refresh_access_token(sp)

        if sp is not None:
            print("Access token refreshed successfully")
        else:
            print("Failed to refresh access token")

if __name__ == "__main__":
    main()