import time

import settings
from locators import BurgerLocators
from data import BurgersServiceTestData
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Создаем класс для тестирования входа через   "Зарегистррироваться"
class TestEnterByFormRegistration:
    def test_registration(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")


# Заполнение полей регистрации
        name_input = driver.find_element(*BurgerLocators.LOGIN_NAME_INPUT)
        name_input.send_keys("Ума")


        email_input=driver.find_element(*BurgerLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(*BurgersServiceTestData.AUTH_EMAIL_RANDOM)


        email_password = driver.find_element(*BurgerLocators.LOGIN_PASSWORD_INPUT)
        email_password.send_keys("123456")


# Клик по кнопке  зарегистрироваться
        btn_regisration= driver.find_element(*BurgerLocators.LOGIN_SUBMIT)
        btn_regisration.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.element_to_be_clickable(BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON))


# Заполнение формы вход
        email_input = driver.find_element(*BurgerLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(*BurgersServiceTestData.AUTH_EMAIL)


        email_password = driver.find_element(*BurgerLocators.LOGIN_PASSWORD_INPUT)
        email_password.send_keys("123456")




# Клик по кнопке  "войти"
        btn_enter = driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON)
        btn_enter.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element(BurgerLocators.TITLE_COLLECT_BURGER, 'Соберите бургер'))
        coll_burg = driver.find_element(*BurgerLocators.TITLE_COLLECT_BURGER)

        assert coll_burg.is_displayed() and coll_burg.text == 'Соберите бургер'