import settings
from conftest import driver
from locators import BurgerLocators
from data import BurgersServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Создаем класс для тестирования формы "Зарегистррироваться"
class TestRegistrstion:
    def test_registration(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

# Заполнение полей регистрации
        name_input = driver.find_element(*BurgerLocators.LOGIN_NAME_INPUT)
        name_input.send_keys("Ума")

        email_input=driver.find_element(*BurgerLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(*BurgersServiceTestData.AUTH_EMAIL_RANDOM)

        email_password = driver.find_element(*BurgerLocators.LOGIN_PASSWORD_INPUT)
        email_password.send_keys("123456")


# Клик по кнопке  "Зарегистрироваться"
        driver.find_element(*BurgerLocators.LOGIN_SUBMIT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.REGISTRATION_TITLE_PERSONAL_ACCOUNT, 'Вход'))
        regisrt_title = driver.find_element(*BurgerLocators.REGISTRATION_TITLE_PERSONAL_ACCOUNT)

        assert regisrt_title.is_displayed() and regisrt_title.text == 'Вход'
