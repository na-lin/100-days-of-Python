from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
import time
# chrome_driver = "C:\Development\chromedriver.exe"

edge_driver = "C:\Development\msedgedriver.exe"
service = Service(edge_driver)
# driver = webdriver.Chrome(service=service)
edge_driver = webdriver.Edge(service=service)

edge_driver.get("http://orteil.dashnet.org/experiments/cookie/")
# #
# # # TODO 1 : find element that is avaible for  click cookie
# # # TODO 2 : while loop to click cookie
# # from current time to 5 sec
# # time = time.time() + 5
#
# def buy_stuff():
#     # find webpage to get element : current money
#     # find webpage to get the stuff price
#     # compare money with each stuff's price, buy the max price that is affortable
#     money = 500
#     item_price = []
#     # find max affortable  & click
#     pass
# timeout_5s = time.time() + 5
# timeout_5min = time.time() + 5 * 60
# print(time)
# while True:
#     # clip webpage
#     if time.time() > timeout_5s:
#         # jump to function  : to buy stuff
#     if time.time() > timeout_5min:
#         # get element : cookies/second
#         # print out score
#         break