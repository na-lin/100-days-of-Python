from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver = "C:\Development\chromedriver.exe"

service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)
# TODO: challenge 1
wiki_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(wiki_url)
# article_count = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# NEW: click
# portal = driver.find_element(by=By.LINK_TEXT, value="All portals")
# portal.click()

# NEW : type character and keyboard
search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# # TODO: challenge 2
# test_url = "http://secure-retreat-92358.herokuapp.com/"
# driver.get(test_url)
# first_name = driver.find_element(by=By.NAME, value="fName")
# first_name.send_keys("test_first_name")
# last_name = driver.find_element(by=By.NAME, value="lName")
# last_name.send_keys("test_last_name")
# email = driver.find_element(by=By.NAME, value="email")
# email.send_keys("test@google.com")
# click_buttom = driver.find_element(by=By.CSS_SELECTOR, value=".btn ")
# click_buttom.click()


# driver.quit()