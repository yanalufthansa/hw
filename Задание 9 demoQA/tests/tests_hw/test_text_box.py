import time
from pages.text_box_page import TextBox


def test_text_box(browser):
    text_box_page = TextBox(browser)

    # a. перейти на страницу https://demoga.com/text-box
    text_box_page.visit()
    # b. записать в поля Full Name, Current Address произвольный текст
    text_box_page.name.send_keys('text_name')
    text_box_page.current_address.send_keys('text_addres')
    # c. нажать на кнопку submit
    text_box_page.submit.click_force()
    time.sleep(2)
    # d. проверить, что снизу появились 2 элемента с нашим текстом
    assert text_box_page.name_2.exist()
    assert text_box_page.current_address.exist()