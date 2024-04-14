import time
import settings
from locators import BurgerLocators
from data import BurgersServiceTestData
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Создаем класс для тестирования кнопки "Выход" в Личном кабинете
class TestExitOnPersAccount:
    def test_registration(self, driver):


# Клик по кнопке "войти в аккаунт"
        btn_login_sumbit_main = driver.find_element(*BurgerLocators.LOGIN_SUBMIT_MAIN)
        btn_login_sumbit_main.click()


# Заполнение полей входа

        email_input = driver.find_element(*BurgerLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(*BurgersServiceTestData.AUTH_EMAIL)


        email_password = driver.find_element(*BurgerLocators.LOGIN_PASSWORD_INPUT)
        email_password.send_keys("123456")



# Клик по кнопке  "войти"
        driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON).click()



# Клик по Личному кабинету
        btn_prs_ac = driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT)
        btn_prs_ac.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.BTN_EXIT_ON_PERSONAL_ACCOUNT, "Выход"))



        driver.find_element(*BurgerLocators.BTN_EXIT_ON_PERSONAL_ACCOUNT).click()


        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON , "Войти"))
        btn_exit = driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON)

        assert btn_exit.is_displayed() and  btn_exit.text == "Войти"