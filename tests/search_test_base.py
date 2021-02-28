from selenium import webdriver

from pages.results.results_page_func import ResultsPageFunc
from pages.search.search_page_func import SearchPageFunc
from tests.base_test import BaseTest


class SearchTestBase(BaseTest):
    search_term = None
    driver = None

    def prerequisites(self):
        self.driver = webdriver.Chrome()

    def run_test(self):
        search_page = SearchPageFunc(driver=self.driver)
        results_page = ResultsPageFunc(driver=self.driver)
        search_page.open()
        search_page.search(self.search_term)
        search_results = results_page.get_search_results_titles()
        false_search_results = results_page.verify_search_results_containts_search_term(search_results, self.search_term)
        if len(false_search_results) > 0:
            for search_result in false_search_results:
                print("Search result: {} doesn't contains search term: {}".format(search_result, self.search_term))
            assert False, "Test Failed, Some of search results are not valid"

    def reorder_env(self):
        self.driver.quit()

