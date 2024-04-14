import settings
from locators import BurgerLocators
from conftest import driver
from conftest import driver
from data import BurgersServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Создаем класс для тестирования перехода между разделами "Конструктора"
class TestTransitionOnChaper:
    def test_registration(self,driver):

# Клик по кнопке "Конструктор"

        button_designer=driver.find_element(*BurgerLocators.BTN_DESIGNER)
        button_designer.click()


# Клик по разделу "Соусы"

        btn_ingredients_sauces=driver.find_element(*BurgerLocators.BURGEST_INGRIDIENTS_SAUCES)
        btn_ingredients_sauces.click()

# Клик по разделу "Начинки"

        btn_ingredients_fillings=driver.find_element(*BurgerLocators.BURGEST_INGRIDIENTS_FILLINGS)
        btn_ingredients_fillings.click()


# Клик по разделу "Булки"
        btn_ingredients_bulko=driver.find_element(*BurgerLocators.BURGEST_INGRIDIENTS_BULKO)
        btn_ingredients_bulko.click()


        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.TITLE_COLLECT_BURGER, 'Соберите бургер'))
        coll_burg = driver.find_element(*BurgerLocators.TITLE_COLLECT_BURGER)

        assert coll_burg.is_displayed() and coll_burg.text == 'Соберите бургер'