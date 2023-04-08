import requests
from bs4 import BeautifulSoup
import os.path
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

memorey_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
year = memorey_date[:4]
billboard_url = f"https://www.billboard.com/charts/hot-100/{memorey_date}/"

# Scraping data from billboard webpage
billboard_response = requests.get(billboard_url)
billboard_response.raise_for_status()
billboard_code = billboard_response.text
soup = BeautifulSoup(billboard_code, "html.parser")
songs = soup.find_all(name="h3", class_="a-no-trucate")
songs_title = [song.getText().strip("\n") for song in songs]


# TODO: when scope = "user-library-read", it will not have exception: Insufficient client scope, reason: None
# TODO: but when scope = "playlist-modify-private", have exception , but can have token.txt
# NEW: solve this problem by add both of them.
# Authorize Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
                                               client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
                                               redirect_uri=os.environ.get("REDIRECT_URL"),
                                               scope="user-library-read,playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               ))
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])


# Get song spotify url
songs_url = []
for song in songs_title:
    # type should be equal to track
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # handle when song not exist in spotify
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_url.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# create a playlist
# Get user id
user_id = sp.current_user()["id"]
playlist_return = sp.user_playlist_create(user=user_id, name=f"{memorey_date} Billboard 100", public=False)
playlist_url = playlist_return["external_urls"]["spotify"]
print(playlist_url)
# add song into playlist
add_result = sp.playlist_add_items(playlist_id=playlist_return['id'],
                      items=songs_url
                      )
pprint(add_result)
