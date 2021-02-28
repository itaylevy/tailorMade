from pages.base_page import BasePage
from pages.search.search_page_locators import SearchPageLocators
from selenium_wrapper.BaseElement.base_element import BaseElement


class SearchPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @property
    def search_field(self):
        return BaseElement(self.driver, SearchPageLocators.SEARCH_FIELD)