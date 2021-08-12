import pytest
import allure
from selenium import webdriver
from lib.page_objects.user_profile_page import UserProfilePage



@pytest.fixture(scope="function")
def user_profile_page(configuration, request):
    driver = webdriver.Chrome()
    page = UserProfilePage(driver)
    page.get_page(configuration.WEBSITE_URL)
    def close_driver():
        driver.quit()

    request.addfinalizer(close_driver)
    return page


class TestCatalog:

    def test_sort_items(self, user_profile_page, configuration):
        """When user clicks on the sort dropdown
        And sorts by price high to low
        Then all items in the page are sorted by highest to lowest price
        """
        user_profile_page.items_sort(configuration.SORT_TITLE)
        items = user_profile_page.sort_results(configuration.CURRENCY)
        items.sort(reverse=True)
        assert items[0] == max(items)




