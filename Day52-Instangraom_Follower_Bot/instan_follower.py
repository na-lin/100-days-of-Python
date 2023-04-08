from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


class InstanFollower:
    def __init__(self, chrome_driver_path):
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path))

    def login(self, login_url, login_username, login_pass):
        self.driver.get(login_url)
        sleep(5)
        # WebDriverWait(self.driver,10).until()
        user_name = self.driver.find_element(by=By.NAME, value="username")
        user_name.clear()
        user_name.send_keys(login_username)
        sleep(2)
        password = self.driver.find_element(by=By.NAME, value="password")
        password.clear()
        password.send_keys(login_pass)
        sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self, target_account):
        sleep(2)
        # dismiss
        save_infor = self.driver.find_element(by=By.XPATH,
                                              value='//*[@id="react-root"]/section/main/div/div/div/div/button')
        save_infor.click()
        sleep(3)

        popup_menu = self.driver.find_element(by=By.CSS_SELECTOR, value="div.piCib")
        notification_dismiss = self.driver.find_element(by=By.XPATH,
                                                        value='/html/body/div[5]/div/div/div/div[3]/button[2]')
        ActionChains(self.driver).move_to_element(popup_menu).click(notification_dismiss).perform()
        sleep(3)

        search = self.driver.find_element(by=By.XPATH,
                                          value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        # search.click()
        ActionChains(self.driver).move_to_element(search).click(search).perform()
        ActionChains(self.driver).move_to_element(search).send_keys(target_account).perform()
        sleep(2)
        ActionChains(self.driver).move_to_element(search).send_keys(Keys.ENTER).perform()
        ActionChains(self.driver).move_to_element(search).send_keys(Keys.ENTER).perform()
        sleep(5)

        # find followers

        followers = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        ActionChains(self.driver).move_to_element(followers).click(followers).perform()
        sleep(2)
        print(followers.text)

        # above is ok
        # TODO: Scoll down
        # HINT :  problem is can't target the pop up dialoge
        popup_dialog = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".isgrP")))
        for i in range(4):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",popup_dialog)


    def follow(self):
        pass
