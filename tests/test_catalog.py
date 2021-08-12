import pytest
import allure
from selenium import webdriver
from lib.page_objects.catalog_page import CatalogPage



@pytest.fixture(scope="function")
def catalog_page(configuration, request):
    driver = webdriver.Chrome()
    page = CatalogPage(driver)
    page.get_page(configuration.WEBSITE_URL)
    def close_driver():
        driver.quit()

    request.addfinalizer(close_driver)
    return page


class TestCatalog:

    def test_search_catalog(self, configuration, catalog_page):
        """ When user clicks on the brand filter dropdown
        And enters “Ni” in the search input
        And select “Nike” brand from the result list
        Then that all items within the result page are with “Nike” brand
        """
        brand = "Nike"
        search_input = "Ni"
        catalog_page.select_filter(configuration.BRAND_FILTER)
        assert catalog_page.search_brand(search_input,brand) == brand
        assert catalog_page.filter_results(brand,configuration.BRAND_FILTER) == True

    def test_filter_by_price_range(self, configuration, catalog_page):
        """ When user clicks on the price filter dropdown
        And enters values between “20” to "50"
        Then that all items within the result page are within the “20” to "50" price range
        """
        from_val = "20"
        to_val = "50"
        catalog_page.select_filter(configuration.PRICE_FILTER)
        catalog_page.search_items_by_price(from_val, to_val, configuration.PRICE_FILTER)
        assert catalog_page.price_filters_displayed() == configuration.FILTER_RESULT
        assert catalog_page.price_result() == True



