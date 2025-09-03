import unittest
# from allure import link
from selenium.webdriver.common.by import By
from utils.driver_manager import DriverManager
from pages.showcase_page import ShowcasePage
import time
import pytest



class TestShowcaseDesigners(unittest.TestCase):                                                                     #Class for testing Showcase Designers
    # @pytest.fixture(autouse=True)
    @classmethod                                                                                                    # Setup method to initialize the driver and page object
    def setUpClass(cls):                                                                                            # Class method to set up the test environment         
        cls.driver = DriverManager.get_driver()
        cls.showcase_page = ShowcasePage(cls.driver)                                                                # Initialize the ShowcasePage with the driver
        
    @classmethod                                                                                                    # Class method to tear down the test environment    
    def tearDownClass(cls):                                                                                         # Class method to clean up after tests
        cls.driver.quit()                                                                                           # Quit the driver after all tests are done

    def test_example_failure(self):                                                                                 # Example test that intentionally fails to demonstrate context handling
        """
        Example test that fails with context
        """
        try:
            # Simulate a failure
            self.assertTrue(self.showcase_page.find_element(*self.showcase_page.HOME_LINK).is_displayed())
            self.showcase_page.find_element(*self.showcase_page.HOME_LINK).click()                                  # Change to fail the test to HOME_LIN
            assert True, "Intentional failure for demonstration"
        except AssertionError as e:
            assert False, "Intentional failure for demonstration"
            # Add additional context to the failure
            # self.request.node.add_marker(
            #     pytest.mark.xfail(reason=f"Failed with context: {str(e)}")
            # )
            raise
        
    def test_page_title(self):
        time.sleep(2)
        self.assertIn("Show case - Designers", self.showcase_page.get_title())

    def test_page_title1(self):
        """Verify page title contains expected text"""
        title = self.showcase_page.get_title()
        assert "Show case - Designers" in title, f"Expected 'Show case - Designers' in title, got '{title}'"

    def test_designer_cards_present(self):
        link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Designers")                                          # Find the link by partial text
        link.click()
        time.sleep(2)
        self.assertGreater(self.showcase_page.get_designer_count(), 0)
        
    def test_search_functionality(self):
        link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Contact")                                            # Find the link by partial text
        link.click()
        time.sleep(2)
        initial_count = self.showcase_page.get_designer_count()
        self.showcase_page.search_designer("Name")
        # filtered_count = self.showcase_page.get_designer_count()
        # self.assertLess(filtered_count, initial_count)

    def test_filter_buttons(self):                                                                                  # Test for filter buttons
        link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Packages")                                           # Find the link by partial text
        link.click()
        time.sleep(2)
        self.showcase_page.click_filter("Sign Up")

        # all_count = self.showcase_page.get_designer_count()
        # self.showcase_page.click_filter("Sign Up")
        # graphic_count = self.showcase_page.get_designer_count()
        # self.assertLess(graphic_count, all_count)


    def test_all_sections_present(self):                                                                            # Test for all sections presence
        self.assertTrue(self.showcase_page.find_element(*self.showcase_page.HOME_LINK).is_displayed())              # Check if Home link is displayed
        self.showcase_page.find_element(*self.showcase_page.HOME_LINK).click()                                      # Click on Home link
        time.sleep(1)                                                                                               # Wait for page to load
        self.assertTrue(self.showcase_page.find_element(*self.showcase_page.SHOWCASE_LINK).is_displayed())          # Check if Showcase link is displayed
        self.showcase_page.find_element(*self.showcase_page.SHOWCASE_LINK).click()                                  # Click on Showcase link
        time.sleep(1)
        self.assertTrue(self.showcase_page.find_element(*self.showcase_page.SERVICES_LINK).is_displayed())          # Check if Services link is displayed
        self.showcase_page.find_element(*self.showcase_page.SERVICES_LINK).click()                                  # Click on Services link
        time.sleep(1)
        self.assertTrue(self.showcase_page.find_element(*self.showcase_page.DESIGNER_LINK).is_displayed())          # Check if Designer link is displayed
        self.showcase_page.find_element(*self.showcase_page.DESIGNER_LINK).click()                                  # Click on Designer link
        time.sleep(1)
        self.assertTrue(self.showcase_page.find_element(*self.showcase_page.PACKAGES_LINK).is_displayed())          # Check if Packages link is displayed
        self.showcase_page.find_element(*self.showcase_page.PACKAGES_LINK).click()                                  # Click on Packages link
        time.sleep(1)
        self.assertTrue(self.showcase_page.find_element(*self.showcase_page.CONTACT_LINK).is_displayed())           # Check if Contact link is displayed 
        self.showcase_page.find_element(*self.showcase_page.CONTACT_LINK).click()                                   # Click on Contact link
        time.sleep(1)

    # def test_modal_functionality(self):
    #     time.sleep(2)
    #     self.showcase_page.open_designer_modal(0)
    #     self.assertTrue(self.showcase_page.find_element(*self.showcase_page.MODAL).is_displayed())
    #     self.showcase_page.close_modal()


if __name__ == "__main__":
    unittest.main()