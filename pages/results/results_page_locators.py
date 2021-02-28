from selenium.webdriver.common.by import By


class ResultsPageLocators(object):
    SEARCH_FIELD = (By.XPATH, ".//input")
    SEARCH_RESULT = (By.XPATH, "//*[@id='rso']/div/div/div/div[1]/a/h3/span")