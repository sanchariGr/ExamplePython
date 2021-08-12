import pytest
import time
from urllib.parse import urljoin
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from page_objects import PageObject, PageElement


class CatalogPage(PageElement):
    PAGE_URL = '/catalog'
    DROPDOWN = '//div[@class="Card_card__21tqh Card_elevated__366Vf"]'
    SEARCH_ITEM = '//div[@class="Card_card__21tqh Card_elevated__366Vf"]//h2[text()="{}"]'
    __country_modal = (By.XPATH, '//div[@class="u-ui-padding-regular u-fill-width"]')
    __cancel_modal = (By.XPATH, '//div[@class="u-ui-padding-regular u-fill-width"]//button')
    __filter_result = (By.XPATH, '//div[@class="ItemBox_details__1c8wh"]//h4')
    __search = (By.ID, 'brand_keyword')
    __dropdown_result = (By.XPATH, '//div[@class="Card_card__21tqh Card_elevated__366Vf"]')
    __brand_filter = (By.XPATH, '//div[@class="u-position-relative"]//button//span//span[text()="{}"]')
    __from_price = (By.ID, 'price_from')
    __to_price = (By.ID, 'price_to')
    __price_filter = (By.XPATH, '//div[@class="u-ui-margin-top-medium"]//div[text()]')
    __price_result = (By.XPATH, '//div[@class="ItemBox_title-content__1LClm"]//h3')

    def __init__(self, driver):
        self.driver = driver

    def wait_until_xpath(self, element):
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
        return True

    def get_page(self, base_url):
        self.driver.get(urljoin(base_url, self.PAGE_URL.format()))
        try:
            self.driver.find_element(*self.__country_modal)
            self.driver.find_element(*self.__cancel_modal).click()
        except:
            pass

    def select_filter(self, data):
        self.driver.find_element_by_xpath('//div[@class="u-position-relative"]//button//span//span[text()="{}"]'.format(data)).click()
        try:
            self.wait_until_xpath(self.DROPDOWN) is True
        except:
            pass

    def search_brand(self, search_name, name):
        self.driver.find_element(*self.__search).send_keys(search_name)
        if self.wait_until_xpath(self.SEARCH_ITEM.format(name)) is True:
            return name

    def filter_results(self, name, data):
        self.driver.find_element_by_xpath('//div[@class="Card_card__21tqh Card_elevated__366Vf"]//h2[text()="{}"]'.format(name)).click()
        self.select_filter(data)
        result = self.driver.find_elements(*self.__filter_result)
        for x in result:
            if x.text == name:
                return True

    def search_items_by_price(self, from_value, to_value, data):
        self.driver.find_element(*self.__from_price).send_keys(from_value)
        self.driver.find_element(*self.__to_price).send_keys(to_value)
        self.select_filter(data)

    def price_filters_displayed(self):
        v = []
        val = self.driver.find_elements(*self.__price_filter)
        for x in val:
            v.append(x.text)
        return v

    def price_result(self):
        v = []
        result = self.driver.find_elements(*self.__price_result)
        for x in result:
            if (x.text >='£20.00' and x.text <= '£50.00' or x.text >= '20,00 €' and x.text <= '50,00 €'):
                return True

