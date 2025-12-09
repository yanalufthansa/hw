from pages.web_tables_page import WebTables
import time


def test_web_tables(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()

    assert web_tables_page.add_button.exist()
    web_tables_page.add_button.click()
    assert web_tables_page.window.exist()
    web_tables_page.submit_button.click()
    assert web_tables_page.window.exist()
    web_tables_page.first_name.send_keys("First_name")
    web_tables_page.last_name.send_keys("Last_name")
    web_tables_page.email.send_keys("email@mail.ru")
    web_tables_page.age.send_keys("25")
    web_tables_page.salary.send_keys("5000")
    web_tables_page.department.send_keys("Moscow")
    web_tables_page.submit_button.click_force()
    assert not web_tables_page.window.exist()
    assert web_tables_page.record.exist()
    web_tables_page.edit_record_button.click()
    assert web_tables_page.window.exist()
    web_tables_page.first_name.clear()
    web_tables_page.first_name.send_keys("First_name")
    web_tables_page.submit_button.click()
    time.sleep(2)
    web_tables_page.delete_button_2.click_force()
    time.sleep(2)