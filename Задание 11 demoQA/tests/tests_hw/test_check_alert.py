from pages.alerts_page import Alerts
import time


def test_check_alert(browser):
    alerts = Alerts(browser)
    alerts.visit()

    # i. на странице присутствует кнопка “#timerAlertButton”
    assert alerts.time_alert_button.exist()

    # ii. через 5 сек после клика на кнопку всплывает алерт
    alerts.time_alert_button.click()
    time.sleep(5)
    assert alerts.alert()
    alerts.alert().accept()