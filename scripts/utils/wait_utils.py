import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from page_objects import PageObject, PageElement

class WaitUtils(PageElement):

## this is a WIP


    def __init__(self, driver):
            self.driver = driver

    def wait_until_xpath(self, element):
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
        return True