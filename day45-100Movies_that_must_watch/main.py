import requests
from bs4 import BeautifulSoup
from pprint import pprint
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
response.raise_for_status()
empire_web_code = response.text
soup = BeautifulSoup(empire_web_code,"html.parser")

title = soup.find_all(name="h3", class_="title")
movie_title = [movie.getText() for movie in title][::-1]

with open("movies.txt", mode="w") as file:
    for movie in movie_title:
        file.write(f"{movie}\n")

