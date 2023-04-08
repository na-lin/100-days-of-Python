from instan_follower import InstanFollower

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SCHELLEY_ACCOUNT = "schelleyyuki_"
USER_NAME = "Olive_ekerin"
PASSWORD = "IGLDoB866N2022"

LOGIN_URL = "https://www.instagram.com/accounts/login/"
bot = InstanFollower(CHROME_DRIVER_PATH)

# TODO 1: login instangram account
bot.login(LOGIN_URL, USER_NAME, PASSWORD)

# # TODO 2 :find follower
bot.find_followers(SCHELLEY_ACCOUNT)
# # TODO 3: follow
# bot.follow()
