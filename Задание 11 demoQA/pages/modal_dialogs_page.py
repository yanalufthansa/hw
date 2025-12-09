from components.WebElement import WebElement
from pages.base_page import BasePage


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, 'header > a')
        self.smallmodal_btn = WebElement(driver, "#showSmallModal")
        self.largemodal_btn = WebElement(driver, "#showLargeModal")
        self.closeSmallmodal = WebElement(driver, "#closeSmallModal")
        self.smallmodal = WebElement(driver, "body > div.fade.modal.show > div > div")
        self.largemodal = WebElement(driver, "body > div.fade.modal.show > div > div")
        self.closeLargemodal = WebElement(driver, "#closeLargeModal")