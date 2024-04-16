import settings
from conftest import driver
from locators import BurgerLocators
from data import BurgersServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Класс для тестирования формы Регистрация
class TestRegistr:
    def test_successful_registrstion(self,driver):

# Переход на страницу регистрации
        driver.find_element(*BurgerLocators.LOGIN_SUBMIT_MAIN).click()
        driver.find_element(*BurgerLocators.LOGIN_SUBMIT_REGISTER).click()

# Заполнение полей регистрации

        name_input = driver.find_element(*BurgerLocators.LOGIN_NAME_INPUT)
        name_input.send_keys(*BurgersServiceTestData.AUTH_NAME)

        email_input = driver.find_element(*BurgerLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(*BurgersServiceTestData.AUTH_EMAIL_RANDOM)

        email_password = driver.find_element(*BurgerLocators.LOGIN_PASSWORD_INPUT)
        email_password.send_keys(*BurgersServiceTestData.AUTH_PASSWORD)


# Клик по кнопке  "Зарегистрироваться"
        driver.find_element(*BurgerLocators.LOGIN_SUBMIT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.REGISTRATION_TITLE_PERSONAL_ACCOUNT, 'Вход'))
        regisrt_title = driver.find_element(*BurgerLocators.REGISTRATION_TITLE_PERSONAL_ACCOUNT)

        assert regisrt_title.is_displayed() and regisrt_title.text == 'Вход'
