# Author - Rayan Hussain

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

# Construct a file path to the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), 'Most Streamed Spotify Songs 2024.csv')

# Read the CSV file with ISO 8859-1 encoding into a data frame
df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

# Initialise Spotipy client with app details
client_credentials_manager = SpotifyClientCredentials(client_id='SPOTIFY_CLIENT_ID', client_secret='SPOTIFY_CLIENT_SECRET')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to fetch cover URL for a given track and artist
def get_cover_url(track_name, artist_name):
    try:
        # Search for the track and artist in Spotify's database
        result = sp.search(q=f"track:{track_name} artist:{artist_name}", type='track')
        # If a match is found, return the URL of the album cover image
        if result['tracks']['items']:
            return result['tracks']['items'][0]['album']['images'][0]['url']
        # Return None if no match is found
        else:
            return None
    # Handle any errors during the API call
    except Exception as e:
        print(f"Error fetching cover for {track_name} by {artist_name}: {e}")
        return None

# Add a new column to the data frame for cover image URLs
for index, row in df.iterrows():
    print(f"Processing {index + 1}/{len(df)}: {row['Track']} by {row['Artist']}...")
    df.at[index, 'cover_url'] = get_cover_url(row['Track'], row['Artist'])

# Save the updated data frame to a new CSV file
output_file_path = os.path.join(os.path.dirname(__file__), 'Most Streamed Spotify Songs 2024 with Covers.csv')
df.to_csv(output_file_path, index=False)

print("CSV file updated with cover URLs.")



