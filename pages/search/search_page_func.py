from pages.search.search_page import SearchPage


class SearchPageFunc(SearchPage):
    def __init__(self, driver):
        SearchPage.__init__(self, driver)

    def open(self):
        self.driver.get(url='https://www.google.com/')

    def search(self, search_term):
        self.search_field.enter_text(txt=search_term)
        self.search_field.click_enter()
