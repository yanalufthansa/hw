from pages.modal_dialogs_page import ModalDialogs
import time


def test_check_modal(browser):
    modal_dialogs = ModalDialogs(browser)

    # i. на странице присутствуют 2 кнопки “Small modal” и “Large modal”
    modal_dialogs.visit()
    assert modal_dialogs.smallmodal_btn.exist()
    assert modal_dialogs.largemodal_btn.exist()

    # ii. при клике на каждую открывается модальное окно
    modal_dialogs.smallmodal_btn.click()
    assert modal_dialogs.smallmodal_btn.exist()
    time.sleep(1)

    # iii. у каждого окна есть кнопка “close” по клику окно закрывается
    assert modal_dialogs.closeSmallmodal.exist()
    modal_dialogs.closeSmallmodal.click()
    time.sleep(1)
    assert not modal_dialogs.smallmodal.exist()

    modal_dialogs.largemodal_btn.click()
    assert modal_dialogs.closeLargemodal.exist()
    assert modal_dialogs.smallmodal.exist()
    modal_dialogs.closeLargemodal.click()
    assert not modal_dialogs.smallmodal.exist()