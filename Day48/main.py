from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_driver = "C:\Development\chromedriver.exe"

# NEW : Get error: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
# driver = webdriver.Chrome(executable_path=chrom_driver)
# driver.get("https://www.bilibili.com/")
# NEW : instead above, in Selenium 4 version , use service object .
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)

# url = 'https://www.bilibili.com/'
# driver.get(url)

# TODO : challenge: extract the upcoming event data from website, store into a nest dictionary time & name
python_org_url = "https://www.python.org/"
driver.get(python_org_url)
# NEW: my solution
# old version
# upcoming_event = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time')
# upcoming_event = driver.find_element(by=By.CSS_SELECTOR, value=".event-widget ul").text
# events = upcoming_event.split("\n")
# events_dict = {int((index - 1) / 2): {"time": events[index - 1], "name": events[index]} for index in
#                range(0, len(events)) if index % 2 == 1}
# print(events_dict)
# NEW: teach's solution
event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
events = {index: {"time": event_times[index].text, "name": event_names[index].text} for index in
          range(len(event_times))}
print(events)

# driver.close()
driver.quit()
