from selenium.webdriver.common.keys import Keys


class BaseElement(object):
    driver = None
    locator = None
    web_element = None

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.find_element()

    def find_element(self):
        self.web_element = self.driver.find_element(*self.locator)

    def find_elements(self):
        return self.driver.find_elements(*self.locator)

    def enter_text(self, txt):
        self.web_element.send_keys(txt)

    def click_enter(self):
        self.web_element.send_keys(Keys.ENTER)