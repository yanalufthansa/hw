from pages.base_page import BasePage
from components.WebElement import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.submit = WebElement(driver, '#submit')
        self.name_2 = WebElement(driver, '#name')