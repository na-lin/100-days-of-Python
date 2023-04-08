from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep


class InternetSpeedTwitterBot:

    def __init__(self, chrome_driver_path):
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path))

    def tweet_at_provider(self, twitter_url, login_email, login_password,msg):
        self.driver.get(twitter_url)
        sleep(20)
        login_by_google = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[2]/span[1]')
        login_by_google.click()

        # swite to login page and switch back to home page when finish login
        base = self.driver.window_handles[0]
        google_login = self.driver.window_handles[1]
        self.driver.switch_to.window(google_login)
        print(self.driver.title)
        email = self.driver.find_element(by=By.NAME, value="identifier")
        email.send_keys(login_email)
        sleep(2)
        next_step_1 = self.driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span')
        next_step_1.click()
        sleep(2)
        password = self.driver.find_element(by=By.NAME, value="PASSWORD_input_name")
        password.send_keys(login_password)
        sleep(2)
        next_step_2 = self.driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span')
        next_step_2.click()
        # back to home page
        self.driver.switch_to.window(base)

        # tweet message
        tweet_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()
        sleep(3)

        content = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        content.send_keys(msg)
        sleep(3)

        send_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        send_button.click()
        sleep(3)

        self.driver.quit()