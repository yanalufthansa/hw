from pages.web_tables_page import WebTables
import time


def test_sort(browser):
    webtable = WebTables(browser)
    webtable.visit()

    # b. при клике на каждый заголовок столбца страницы, происходит сортировка таблицы по этому столбцу
    for element in webtable.header_resize.find_elements():
        time.sleep(2)
        element.click()
        # (Для проверки сортировки, в данном кейсе, достаточно считывать соответствующий класс элемента)
        assert element.get_dom_attribute("class") == "rt-th rt-resizable-header -sort-asc -cursor-pointer"
        time.sleep(2)
    time.sleep(5)