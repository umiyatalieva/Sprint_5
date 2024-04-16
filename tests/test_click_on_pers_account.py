import settings
from locators import BurgerLocators
from data import BurgersServiceTestData
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Создаем класс для тестирования перехода по клику в "Личный кабинет"
class TestClickGoToPersonalAccount:

# Тестирование перехода через Личный кабинет
    def test_click_goto_pers_account(self, driver): # исправлено


# Клик по кнопке "войти в аккаунт"
        btn_login_sumbit_main = driver.find_element(*BurgerLocators.LOGIN_SUBMIT_MAIN)
        btn_login_sumbit_main.click()


# Заполнение полей входа

        email_input = driver.find_element(*BurgerLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(*BurgersServiceTestData.AUTH_EMAIL)


        email_password = driver.find_element(*BurgerLocators.LOGIN_PASSWORD_INPUT)
        email_password.send_keys(*BurgersServiceTestData.AUTH_PASSWORD)


# Клик по кнопке  "войти"
        driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON).click()


# Клик по кнопке "Личный кабинет"
        btn_login_sumbit_main = driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT)
        btn_login_sumbit_main.click()


        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.TITLE_PROFILE , 'Профиль'))
        pers_account = driver.find_element(*BurgerLocators.TITLE_PROFILE)

        assert pers_account.is_displayed() and pers_account.text == 'Профиль'