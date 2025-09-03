from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config


class ShowcasePage(BasePage):                                           # ShowcasePage class for interacting with the showcase page
    # Updated Locators
    DESIGNER_LINK = (By.PARTIAL_LINK_TEXT, "Designer")                  # Locator for designer links
    SEARCH_INPUT = (By.NAME, "Name")                                    # Locator for search input field
    FILTER_BUTTONS = (By.PARTIAL_LINK_TEXT, "Sign Up")                  # Locator for filter buttons
    MODAL = (By.CSS_SELECTOR, ".modal.fade.show")                       # Locator for modal
    MODAL_CLOSE = (By.CSS_SELECTOR, ".modal-header .close")             # Locator for modal close button
    HOME_LINK = (By.PARTIAL_LINK_TEXT, "Home")                          # Locator for home link
    SHOWCASE_LINK = (By.PARTIAL_LINK_TEXT, "Showcase")                  # Locator for showcase link
    SERVICES_LINK = (By.PARTIAL_LINK_TEXT, "Services")                  # Locator for services link
    DESIGNER_LINK = (By.PARTIAL_LINK_TEXT, "Designers")                 # Locator for designers link
    PACKAGES_LINK = (By.PARTIAL_LINK_TEXT, "Packages")                  # Locator for packages link
    CONTACT_LINK = (By.PARTIAL_LINK_TEXT, "Contact")                    # Locator for contact link

    # Constructor to initialize the page
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Config.BASE_URL)
        
    def get_designer_count(self):
        return len(self.find_elements(*self.DESIGNER_LINK))
        
    def search_designer(self, search_text):
        search_box = self.find_element(*self.SEARCH_INPUT)
        search_box.send_keys(search_text)
        # search_box.clear()
        # search_box.send_keys(search_text)
        
    def click_filter(self, filter_name):

        link = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div[2]/ul/li[8]/button")  # Find the link by partial text
        link.click()

        
    def open_designer_modal(self, index=0):
        cards = self.find_elements(*self.DESIGNER_LINK)
        if index < len(cards):
            cards[index].click()
            self.wait_for_element(*self.MODAL)
        else:
            raise IndexError(f"Designer card index {index} out of range")
            
    def close_modal(self):
        self.find_element(*self.MODAL_CLOSE).click()
        self.wait_for_element_to_disappear(*self.MODAL)