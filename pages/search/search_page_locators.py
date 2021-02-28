from selenium.webdriver.common.by import By


class SearchPageLocators(object):
    SEARCH_FIELD = (By.XPATH, "//input[@title='Search']")