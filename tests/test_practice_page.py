import pytest
from pages.homepage import HomePage

@pytest.mark.usefixtures("setup")
class TestHomePage:
    def test_print_title(self):
        homepage = HomePage(self.driver)
        title = homepage.get_title()
        assert title is not None, f"Page title is: {title}"
        #
