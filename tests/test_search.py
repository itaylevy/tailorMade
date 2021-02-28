import pytest

from tests.search_test_base import SearchTestBase


class SearchTests(SearchTestBase):

    @pytest.mark.search
    def test_search_michael_jordan(self):
        self.search_term = 'Michael Jordan'
        self.play_test()