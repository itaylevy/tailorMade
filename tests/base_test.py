from abc import abstractmethod


class BaseTest(object):

    def play_test(self):
        try:
            self.prerequisites()
            self.run_test()
            self.reorder_env()
        except Exception as e:
            raise e

    @abstractmethod
    def prerequisites(self):
        pass

    @abstractmethod
    def run_test(self):
        pass

    @abstractmethod
    def reorder_env(self):
        pass