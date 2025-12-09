from pages.deno_qa_page import DemoQAPage
from pages.elements_page import ElementsPage


def test_footer_text(browser):
    """
    2. в файле test_check_text.py реализуйте тест кейс:
    a. перейти на страницу 'https://demoqa.com/'
    b. проверить что текст в подвале == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    """

    demo_qa_page = DemoQAPage(browser)
    # a. перейти на страницу 'https://demoqa.com/'
    demo_qa_page.visit()
    assert demo_qa_page.footer_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_center_text_on_elements_page(browser):
    """
    3. в файле test_check_text.py реализуйте тест кейс:
    a. перейти на страницу 'https://demoqa.com/'
    b. через кнопку перейти на страницу 'https://demoqa.com/elements'
    c. проверить что текст по центру == 'Please select an item from left to start practice.'
    """
    elements_page = ElementsPage(browser)
    demoqa_page = DemoQAPage(browser)
    demoqa_page.visit()
    expected_center_text = "Please select an item from left to start practice."
    demoqa_page.btn_elements.click()
    assert elements_page.text_center.get_text() == expected_center_text

