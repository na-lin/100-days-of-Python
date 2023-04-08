import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from pprint import pprint
import html

LOWEST_PRICE = 300
EMAIL_USER = "auteforpt@yahoo.com"
EMAIL_PASSWORD = "ojkzycsdcocwfask"
# TODO 1: scrapping from amazon web page
PRODUCT_URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
browser_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
}
amazon_response = requests.get(url=PRODUCT_URL, headers=browser_header)
amazon_response.raise_for_status()
amazon_html_code = amazon_response.text
# TODO 2: make soup to get price in web page
# hint : use lxml parser instead of html.parser
soup = BeautifulSoup(amazon_html_code, "html.parser")
product_name = soup.find(name="span", id="productTitle",
                         class_="a-size-large product-title-word-break").getText().strip(" ")
price = float(soup.find(name="span", class_="a-size-base a-color-price").getText().strip("$"))

# TODO 3: send email alert when price is lower than lowest price
if price < LOWEST_PRICE:
    message = f"{product_name.encode('ascii',errors='xmlcharrefreplace')} is now ${price}\n{PRODUCT_URL}"
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_USER, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL_USER,
                            to_addrs=EMAIL_USER,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}")
