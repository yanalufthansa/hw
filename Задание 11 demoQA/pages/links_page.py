from pages.base_page import BasePage
from components.WebElement import WebElement


class LinksPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/links"
        super().__init__(driver, self.base_url)

        # Ссылка "Home"
        self.home_link = WebElement(driver, "#simpleLink")
