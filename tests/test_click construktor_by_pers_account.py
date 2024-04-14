import settings
from locators import BurgerLocators
from conftest import driver

from data import BurgersServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



# Создаем класс для тестирования перехода в "Конструктор" и по надписи Stellar Burgers через Личном кабинете
class TestClickBtnPersonalAccount:
    def test_registration(self,driver):

# Клик по кнопке "Личный кабинет"
       btn_login_sumbit_main = driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT)
       btn_login_sumbit_main.click()


# Заполнение полей входа

       driver.find_element(*BurgerLocators.LOGIN_EMAIL_INPUT).send_keys(*BurgersServiceTestData.AUTH_EMAIL)
       driver.find_element(*BurgerLocators.LOGIN_PASSWORD_INPUT).send_keys("123456")

       WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
       EC.text_to_be_present_in_element(BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON , "Войти"))



# Клик по кнопке  "войти"
       driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON).click()



# Клик по кнопке "Конструктор"

       button_designer = driver.find_element(*BurgerLocators.BTN_DESIGNER_TWO)
       button_designer.click()


       WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.TITLE_COLLECT_BURGER, 'Соберите бургер'))
       coll_burg = driver.find_element(*BurgerLocators.TITLE_COLLECT_BURGER)

       assert coll_burg.is_displayed() and coll_burg.text == 'Соберите бургер'