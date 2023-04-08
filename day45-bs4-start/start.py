from bs4 import BeautifulSoup
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents,'html.parser')

# get first element's text
title = soup.title.string
# print(title)

# find all anchor tag, include text, attribute
# all_anchor_tag = soup.find_all(name="a")
# print(all_anchor_tag)
#
# for tag in all_anchor_tag:
#     print(tag.name)
#     print(tag.getText())
#     print(tag.get("href"))

# find 1st more specfic
heading = soup.find(name="h1", id="name")
print(heading)

heading_h3 = soup.find_all(name="h3", class_="heading")
print(heading_h3)

# select specific element
sepecific = soup.select(selector=".heading")
print(sepecific)