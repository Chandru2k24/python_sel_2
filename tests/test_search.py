import pytest
from selenium.webdriver.common.by import By
from pages.HomePage import HomePage
from pages.searchpage import SearchPage

@pytest.mark.usefixtures("setup_and_teardown")
class Testsearch:
    def test_search_for_valid_product(self):
        home_page=HomePage(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        home_page.click_search_button()
        search_page=SearchPage(self.driver)
        search_page.display_status_valid_product()