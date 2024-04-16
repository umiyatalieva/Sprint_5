import settings
from locators import BurgerLocators
from conftest import driver
from data import BurgersServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



# Создаем класс дл тестирования перехода через Личный кабинет
class TestOnPersonalAccount:

# Тестирование перехода по надписи Stellar Burger
   def test_goto_stellar_burger(self,driver):

# Клик по кнопке Личный кабинет

        btn_login_sumbit_main = driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT)
        btn_login_sumbit_main.click()


# Заполнение полей входа

        driver.find_element(*BurgerLocators.LOGIN_EMAIL_INPUT).send_keys(*BurgersServiceTestData.AUTH_EMAIL)
        driver.find_element(*BurgerLocators.LOGIN_PASSWORD_INPUT).send_keys("123456")

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON , "Войти"))



# Клик по кнопке  "войти"
        driver.find_element(*BurgerLocators.LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON).click()



# Клик по надписи "Stellar Burgers"
        button_stellar_burgers=driver.find_element(*BurgerLocators.CLICK_IN_STELLAR_BYRGERS_TWO)
        button_stellar_burgers.click()


        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.TITLE_COLLECT_BURGER, 'Соберите бургер'))
        coll_burg = driver.find_element(*BurgerLocators.TITLE_COLLECT_BURGER)

        assert coll_burg.is_displayed() and coll_burg.text == 'Соберите бургер'