import pytest
from pages.homepage import HomePage

@pytest.mark.usefixtures("setup")
class TestHomePage:
    def test_homepage_loaded(self):
        homepage = HomePage(self.driver)
        # Verify title
        assert homepage.get_title() == "Practice Page"
        # Verify page fully loaded
        homepage.wait_for_page_load()
        # Verify header displayed
        assert homepage.is_header_displayed()