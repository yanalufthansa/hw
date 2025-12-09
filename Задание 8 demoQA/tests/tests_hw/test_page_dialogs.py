import time

from pages.modal_dialogs_page import ModalDialogs


def test_modal_elements(browser):
    # ii. в тестовом файле создайте объект новой страницы
    modal_dialog_page = ModalDialogs(browser)

    # iii. от объекта вызовите метод входа на страницу
    modal_dialog_page.visit()
    # b. проверить, что кнопок подменю, на странице - 5 шт
    # ii. в тестовом файле обратитесь к объекту страницы - к элементу - вызовите метод проверки кол-ва элементов
    assert modal_dialog_page.btns_menu.check_count_elements(count=5)


def test_navigation_modal(browser):
    # ii. создайте объект новой страницы
    modal_dialog_page = ModalDialogs(browser)

    # iii. от объекта вызовите метод входа на страницу
    modal_dialog_page.visit()
    # b. обновить страницу
    modal_dialog_page.refresh()
    # c. перейти на главную страницу через иконку
    modal_dialog_page.icon.click()
    # d. сделать шаг назад стрелкой браузера
    modal_dialog_page.back()
    time.sleep(2)
    # e. установить размеры экрана 900x400
    browser.set_window_size(900, 400)
    # f. сделать шаг вперед стрелкой браузера
    modal_dialog_page.forward()
    time.sleep(2)
    # g. вызвать проверку урла на главной странице
    assert modal_dialog_page.get_url() == "https://demoqa.com/"
    # h. проверить title на главной
    assert browser.title == "DEMOQA"
    # i. вернуть размеры экрана по умолчанию 1000x1000
    browser.set_window_size(1000, 1000)
