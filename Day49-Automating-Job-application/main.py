from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
EMAIL = "lna483018@gmail.com"
PASSWORD = "Wulinaina98"
JOB_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
chrome_driver = "C:\Development\chromedriver.exe"
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)
driver.get(JOB_URL)

# todo 1: log in linkedin
log_in = driver.find_element(by=By.LINK_TEXT, value="登录")
log_in.click()
email_input = driver.find_element(by=By.NAME, value="session_key")
email_input.send_keys(EMAIL)
password_input = driver.find_element(by=By.NAME, value="session_password")
password_input.send_keys(PASSWORD)
check_button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn__primary--large")
check_button.click()

time.sleep(1)

# todo 2: apply for a job
# easy_apply = driver.find_element(by=By.CSS_SELECTOR, value="div.jobs-apply-button--top-card")
# easy_apply.click()
# mobile_number = driver.find_element(by=By.ID, value="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2923865231,44854213,phoneNumber~nationalNumber)")
# mobile_number.send_keys("123456789")
# next_button = driver.find_element(by=By.ID, value="ember357")
# # next_button.click()
# # TODO : find review button & click it
# # TODO : find submit application button & click it

# TODO 3: apply for all job
# TODO 3.1 : Get list apply in this page
job_search_result_list = driver.find_elements(by=By.CSS_SELECTOR, value="a.job-card-container__link.job-card-list__title")
for job in job_search_result_list:
    try:
        easy_apply_button = driver.find_element(by=By.CSS_SELECTOR, value="button.jobs-apply-button")
        easy_apply_button.click()
        # enter phone number if mobile phone text is empty
        mobile_number = driver.find_element(by=By.ID,
                                            value="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2923865231,44854213,phoneNumber~nationalNumber)")
        if mobile_number.text == "":
            mobile_number.send_keys("123456789")

    except NoSuchElementException:
        continue
    else:
        try:
            submit_button = driver.find_element()
            submit_button.click()
        except NoSuchElementException:
            # when there is no button " submit_button " , if it is next button
            # find click exit button  & click
            # find discard button & click
            continue










# click exit :
# artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view
            # submit_button = driver.find_element(by=,value=)
            # submit_button.click()

