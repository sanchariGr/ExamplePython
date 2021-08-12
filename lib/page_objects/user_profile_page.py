import pytest
import time
from urllib.parse import urljoin
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from page_objects import PageObject, PageElement


class UserProfilePage(PageElement):
    PAGE_URL = '/member/64678795'
    DROPDOWN = 'u-ui-padding-vertical-x-small'
    __country_modal = (By.XPATH, '//div[@class="u-ui-padding-regular u-fill-width"]')
    __cancel_modal = (By.XPATH, '//div[@class="u-ui-padding-regular u-fill-width"]//button')
    __select_sort = (By.XPATH, '//li[@class="pile__element"]//span[text()="Price: high to low"]')
    __sort_results = (By.XPATH, '//div[@class="ItemBox_title-content__1LClm"]//h3')

    def __init__(self, driver):
        self.driver = driver

    def wait_until_xpath(self, element):
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
        return True

    def scroll_to_locate(self):
        self.driver.execute_script("window.scrollTo(0, 300)")

    def get_page(self, base_url):
        self.driver.get(urljoin(base_url, self.PAGE_URL.format()))
        try:
            self.driver.find_element(*self.__country_modal)
            self.driver.find_element(*self.__cancel_modal).click()
        except:
            pass

    def sort_dropdown(self, data):
        self.scroll_to_locate()
        self.driver.find_element_by_xpath('//div[@class="u-position-relative"]//span[text()="{}"]'.format(data)).click()
        try:
            self.wait_until_xpath(self.DROPDOWN) is True
        except:
            pass

    def items_sort(self, data):
        self.sort_dropdown(data)
        self.driver.find_element(*self.__select_sort).click()

    def sort_results(self, currency):
        v = []
        results = self.driver.find_elements(*self.__sort_results)
        for x in results:
            v.append(x.text.strip(currency))
        return v

