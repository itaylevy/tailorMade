from pages.base_page import BasePage
from pages.results.results_page_locators import ResultsPageLocators
from selenium_wrapper.BaseElement.base_element import BaseElement


class ResultsPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @property
    def search_result(self):
        return BaseElement(self.driver, ResultsPageLocators.SEARCH_RESULT)

    @property
    def search_field(self):
        return BaseElement(self.driver, ResultsPageLocators.SEARCH_FIELD)