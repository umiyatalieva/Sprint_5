import settings
from locators import BurgerLocators
from data import BurgersServiceTestData
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Создаем класс для тестирования входа через "Восстановить пароль"
class TestFormForgotPassword:
    def test_registration(self,driver):

# Клик по кнопке "войти в аккаунт"
        btn_login_sumbit_main=driver.find_element(*BurgerLocators.LOGIN_SUBMIT_MAIN)
        btn_login_sumbit_main.click()

# Клик по "Восстановить пароль"
        btn_sumbit_recover_password=driver.find_element(*BurgerLocators.LOGIN_SUBMIT_RECOVER_PASSWORD)
        btn_sumbit_recover_password.click()


# Клик по "Войти" в форме "Восстаноить пароль"
        btn_login_sumbit_recover_password=driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON_PASSWORD)
        btn_login_sumbit_recover_password.click()


# Заполнение полей входа

        email_input=driver.find_element(*BurgerLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(*BurgersServiceTestData.AUTH_EMAIL)


        email_password = driver.find_element(*BurgerLocators.LOGIN_PASSWORD_INPUT)
        email_password.send_keys("123456")


# Клик по кнопке  "войти"
        driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON).click()



        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.REGISTRATION_TITLE_PERSONAL_ACCOUNT, 'Вход'))
        text_enter = driver.find_element(*BurgerLocators.REGISTRATION_TITLE_PERSONAL_ACCOUNT)

        assert text_enter.is_displayed() and text_enter.text == 'Вход'