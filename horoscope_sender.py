#!/usr/local/bin/python3
import time
import horoscope_fetcher as hf
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


DRIVER_LOCATION = '/Users/lalit/Documents/chromedriver'
URL = 'https://web.whatsapp.com/'
HOROSCOPE_DICT = {
    'user1': 'h_name1',
    'user2': 'h_name2',
}


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(DRIVER_LOCATION, options=options)
    driver.get(URL)
    wait = WebDriverWait(driver, 120)
    return driver


def send_message(driver, name, message):
    receiver_path = "//span[@title=" + name + "]"
    receiver_box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, receiver_path))
    )
    receiver_box.click()

    cls_name = '_3u328 copyable-text selectable-text'
    xpath_1 = "//div[contains(@class, '_3u328 copyable-text')"
    xpath_2 = " and "
    xpath_3 = "contains(@class ,'selectable-text')]"
    message_path = xpath_1 + xpath_2 + xpath_3
    message_box = driver.find_element_by_xpath(message_path)
    message_box.click()
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    time.sleep(5)  # time to type message and send


if __name__ == '__main__':
    driver = get_driver()
    for u_name, h_name in HOROSCOPE_DICT.items():
        par_url = hf.add_name_in_url(h_name)
        url = hf.add_date_in_url(par_url)
        soup = hf.get_soup(url)
        horoscope = hf.get_horoscope(soup)
        header = hf.get_header(soup, h_name)
        message = hf.get_message(header, horoscope)
        name = "'{}'".format(u_name)
        send_message(driver, name, message)
    driver.quit()