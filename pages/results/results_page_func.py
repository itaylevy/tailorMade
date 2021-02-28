from pages.results.results_page import ResultsPage


class ResultsPageFunc(ResultsPage):
    def __init__(self, driver):
        ResultsPage.__init__(self, driver)

    def get_search_results_titles(self):
        search_results = self.search_result.find_elements()
        search_results_list = list()
        for search_result in search_results:
            search_results_list.append(search_result.text)
        return search_results_list

    def verify_search_results_containts_search_term(self, search_results, search_term):
        false_search_results = list()
        for search_result in search_results:
            if not search_result.lower().__contains__(search_term.lower()):
                false_search_results.append(search_result)
        return false_search_results