from bs4 import BeautifulSoup
import requests
from pprint import pprint

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_text = [tag.getText() for tag in articles]
article_link = [tag.get("href") for tag in articles]

article_upvotes = soup.find_all(name="span", class_="score")
article_scores = [int(score.getText().split()[0]) for score in article_upvotes]
# print(article_text)
# print(article_link)
# print(article_scores)
# TODO: find the highest number of upvote , print out it's link and title
# max_score = max(article_scores)
# if article_scores.count(max_score) == 1:
#     max_score_index = article_scores.index(max_score)
#     print(article_text[max_score_index])
#     print(article_link[max_score_index])

test = [11, 500, 1,2,3,500]

