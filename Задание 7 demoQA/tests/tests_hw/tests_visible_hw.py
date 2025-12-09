from pages.accordion_page import Accordion
import time


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    # ii. проверьте, что элемент #section1Content > p виден
    assert accordion_page.element.visible()
    # iii. кликните на #section1Heading
    accordion_page.element_section1.click()
    # iv. После клика добавьте time.sleep(2)
    time.sleep(2)
    # v. проверьте, что элемент #section1Content > p HE виден
    # 11. добавьте проверку на видимость элемента и добавьте отрицание (элемент уже есть)
    assert not accordion_page.element_section1_check.visible()


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    # ii. проверьте, что следующие элементы по умолчанию скрыты
    # 1. #section2Content > p:nth-child(1)
    # 2. #section2Content > p:nth-child(2)
    # 3. #section3Content > p
    # b. в тесте вызовите проверку видимости для каждого
    # c. в каждую проверку добавьте отрицание
    assert not accordion_page.element_section2_child1.visible()
    assert not accordion_page.element_section2_child2.visible()
    assert not accordion_page.element_section3.visible()