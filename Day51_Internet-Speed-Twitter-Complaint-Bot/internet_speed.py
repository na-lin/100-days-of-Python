from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from time import sleep


class InternetSpeed:
    def __init__(self, edge_driver_path):
        self.driver = webdriver.Edge(service=Service(edge_driver_path))
        self.down = 0
        self.up = 0
        self.get_internet_speed()

    def get_internet_speed(self):
        speedtest_url = "https://www.speedtest.net/"
        self.driver.get(speedtest_url)
        sleep(10)
        start_test = self.driver.find_element(by=By.XPATH,
                                              value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_test.click()
        sleep(60)
        self.down = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.down)
        print(self.up)

        self.driver.quit()