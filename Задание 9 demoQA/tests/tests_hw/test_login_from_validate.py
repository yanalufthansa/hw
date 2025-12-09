from pages.form_page import FormPage
import time


def test_login_form_validate(browser):
    form_page = FormPage(browser)

    # a. перейти на страницу https://demoga.com/automation-practice-form
    form_page.visit()
    # b. проверить плейсхолдер у полей
    # i. first_name
    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    # ii. last_name
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    # iii. user_email - также проверьте атрибут “pattern”
    assert form_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert form_page.user_email.get_dom_attribute('pattern') == ("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")

    # c. Сделайте попытку отправки пустой формы и проверьте наличие класса “was-validated” у элемента формы
    form_page.btn_submit.click_force()
    time.sleep(2)
    assert form_page.user_form.get_dom_attribute('class') == 'was-validated'