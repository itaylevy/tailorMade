class BasePage(object):
    driver = None

    def __init__(self, driver):
        self.driver = driver

