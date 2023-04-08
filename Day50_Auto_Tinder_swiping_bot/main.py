from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
import time
# chrome_driver = "ChromeDriver Path in computer "
chrome_driver = "C:\Development\chromedriver.exe"
# tinter url = "https://tinder.com/"
# TINTER_URL = "Tinder URL"
TINTER_URL = "https://tinder.com/"
EMAIL = "Dummy@google.com"
PASSWORD = "Dummy123"

service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)
driver.get(TINTER_URL)
# TODO 1 : log in with google or facebook accrount
# //*[@id="q-1330521921"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a
time.sleep(10) # leave a little time for webpage to display
log_in_button = driver.find_element(by=By.XPATH, value='//*[@id="q-1330521921"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()
time.sleep(4)
facebook_log = driver.find_element(by=By.XPATH, value='//*[@id="q1236064299"]/div/div/div[1]/div/div[3]/span/div[2]/button')
time.sleep(2)
facebook_log.click()

# TODO 2 : LOGIN WITH facebook in new pop up window
# work in new window -- switch to window in front
identification_windows = driver.window_handles
base_window = identification_windows[0]
# new windows that pop up from base window
fb_login_window = identification_windows[1]
# switch selenium to target the new window
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(2)
email_input = driver.find_element(by=By.NAME, value="email")
email_input.send_keys(EMAIL)
password_input = driver.find_element(by=By.NAME, value="pass")
password_input.send_keys(PASSWORD)
login_input = driver.find_element(by=By.NAME, value="login")
# login_input.click()

# revert back to base window
driver.switch_to.window(base_window)
print(driver.title)

# TODO 3 : dismiss all requests
time.sleep(5)
location_allow = driver.find_element(by=By.XPATH, value="allow button xpath")
location_allow.click()
time.sleep(3)

notification_not_interested = driver.find_element(by=By.XPATH, value="not interested xpath")
notification_not_interested.click()
time.sleep(3)

cookie_accept = driver.find_element(by=By.XPATH, value="cookie accept xpath")
cookie_accept.click()

# TODO 4 : hit like  & delay 1 second
allow_click = 100
while allow_click > 0:
    time.sleep(1)
    try:
        like_button = driver.find_element(by=By.XPATH, value="like button xpaht")
        like_button.click()
        allow_click -= 1
    except NoSuchElementException:
        time.sleep(2)
        continue
    # catch situation : when a match pop up in same window then hide like button
    # implies that the desired element wasn't clickable as some other element obscures it.
    except ElementClickInterceptedException:
        back_to_tinder = driver.find_element(by=By.XPATH, value="back to tinder button")
        back_to_tinder.click()


driver.quit()