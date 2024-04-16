import time

import settings
from conftest import driver
from locators import BurgerLocators
from data import BurgersServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Создаем класс для тестирования входа
class TestLogin:

# Тестирование вход через "Личный кабинет"
    def test_enter_on_personal_account(self,driver):


# Клик по кнопке "Личный кабинет"

       btn_pers_acc=driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT)
       btn_pers_acc.click()

# Заполнение полей входа

       driver.find_element(*BurgerLocators.LOGIN_EMAIL_INPUT).send_keys(*BurgersServiceTestData.AUTH_EMAIL)
       driver.find_element(*BurgerLocators.LOGIN_PASSWORD_INPUT).send_keys(*BurgersServiceTestData.AUTH_PASSWORD)

       WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
       EC.text_to_be_present_in_element(BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON , "Войти"))



# Клик по кнопке  "войти"
       driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON).click()


       WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
       EC.text_to_be_present_in_element(BurgerLocators.TITLE_COLLECT_BURGER, 'Соберите бургер'))
       coll_burg = driver.find_element(*BurgerLocators.TITLE_COLLECT_BURGER)

       assert coll_burg.is_displayed() and coll_burg.text == 'Соберите бургер'

