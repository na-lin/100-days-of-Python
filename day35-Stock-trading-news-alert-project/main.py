import requests
from twilio.rest import Client
from bs4 import BeautifulSoup

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
symbol = ""
STOCK_DIFFERENT = 5
NUMBER_OF_NEW = 3

def get_stoke_change():
    ## TODO: STEP 1: Use https://www.alphavantage.co ， API : TIME_SERIES_DAILY
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": "GNOYDNZ3RZXDK84C",
        "outputsize": "compact",
    }
    stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
    stock_response.raise_for_status()
    stock_data = stock_response.json()

    stock_datetime = [item for item in stock_data["Time Series (Daily)"]]
    yesterday_close_price = float(stock_data["Time Series (Daily)"][stock_datetime[0]]["4. close"])
    day_before_yesterday_close_price = float(stock_data["Time Series (Daily)"][stock_datetime[1]]["4. close"])

    stock_change = (abs(yesterday_close_price - day_before_yesterday_close_price) / yesterday_close_price) * 100

    global symbol

    if yesterday_close_price - day_before_yesterday_close_price < 0:
        symbol = "🔻"
    else:
        symbol = "🔺"
    return stock_change


def get_news():
    """get news of Company from NEWAPI, return the new in english """
    ## TODO: STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_url = "https://newsapi.org/v2/everything"
    news_api_key = "de1a2825ad334ba5a375a1d5b526ba3b"
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": news_api_key,
        "searchIn":"title",
        "language": 'en',
    }
    news_response = requests.get(url=news_url, params=news_parameters)
    news_response.raise_for_status()
    news = news_response.json()
    return news


def send_sms(stock_change, new):
    ## TODO 3: STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    account_sid = "AC533ce877dd8c0c2ed97afdf136833441"
    auth_token = "9e55c738bcb90897e584c6c8311f73ec"

    content = ""
    for _ in range(NUMBER_OF_NEW):
        content += f"{STOCK}:{symbol}{round(stock_change)}%" \
                   f"\n\nheadline:{new['articles'][_]['title']}" \
                   f"\n\nBrief:{new['articles'][_]['description']}\n\n"

    print(BeautifulSoup(content, features="html.parser").text)

    client = Client(account_sid, auth_token)
    message = client.messages.create(body=BeautifulSoup(content, features="html.parser").text,
                                     from_="+18456689981",
                                     to="+16463318838")


if get_stoke_change() > STOCK_DIFFERENT:
    news = get_news()
    send_sms(get_stoke_change(), news)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
