import time
from pages.links_page import LinksPage


def test_new_tab(browser):
    links_page = LinksPage(browser)

    # a. Страница https://demoqa.com/links
    links_page.visit()

    # b. На странице имеется ссылка “Home”
    assert links_page.home_link.exist()

    # c. текст ссылки == “Home”
    assert links_page.home_link.get_text() == "Home"

    # d. href ссылки == “https://demoga.com”
    assert links_page.home_link.get_dom_attribute('href') == "https://demoqa.com"

    # e. При клике на ссылку открывается новая вкладка
    original_window = browser.current_window_handle
    links_page.home_link.click()
    time.sleep(2)

    # Проверяем, что количество вкладок увеличилось
    assert len(browser.window_handles) == 2

    # Переключаемся на новую вкладку и проверяем URL
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == "https://demoqa.com/"

    # Закрываем новую вкладку и возвращаемся к исходной
    browser.close()
    browser.switch_to.window(original_window)