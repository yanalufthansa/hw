from pages.base_page import BasePage
from components.WebElement import WebElement


class Accordion(BasePage):

    def __init__(self, driver):
        # 3. для этого в папке pages создайте файл accordion_page.py
        # 4. в файле реализуйте класс страницы Accordion, по аналогии с классами DemoQa и ElementsPage
        # 5. Отличается только название, урл и элементы
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        # 7. в новом классе страницы добавьте элемент с указанным локатором
        self.element = WebElement(driver, '#section1Content > p')
        # 9. в новом классе страницы добавьте элемент с указанным локатором
        self.element_section1 = WebElement(driver, '#section1Heading')
        self.element_section1_check = WebElement(driver, '#section1Content > p')

        # 4a. Создайте каждый элемент в классе страницы
        self.element_section2_child1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.element_section2_child2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.element_section3 = WebElement(driver, '#section3Content > p')