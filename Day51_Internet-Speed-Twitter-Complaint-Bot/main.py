from internet_speed_twitter_bot import InternetSpeedTwitterBot
from internet_speed import InternetSpeed

# NEW: Project describe:
# use speedtest website working out download speed and upload speed with result id
# compare these against your ISP
# Twitter your ISP to make a complain
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
EDGE_DRIVER_PATH = "C:\Development\msedgedriver.exe"
TWITTER_EMAIL = "lna483018@gmail.com"
TWITTER_PASSWORD = "NewWulinaina9976ai"
TWITTER_URL = "https://twitter.com/i/flow/signup"

internet_speed = InternetSpeed(edge_driver_path=EDGE_DRIVER_PATH)
down_speed = float(internet_speed.down)
up_speed = float(internet_speed.up)

if down_speed < PROMISED_DOWN or up_speed < PROMISED_UP:
    msg = f"Hey Internet Provider, why is my internet speed {down_speed}down/{up_speed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

    bot = InternetSpeedTwitterBot(chrome_driver_path=CHROME_DRIVER_PATH)
    tweet_to_provide = bot.tweet_at_provider(TWITTER_URL, TWITTER_EMAIL, TWITTER_PASSWORD,msg)
else:
    print("Your internet speed is not less than internet provider guaranteed speed.")