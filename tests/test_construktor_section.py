import settings
from locators import BurgerLocators
from conftest import driver
from conftest import driver
from data import BurgersServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Создаем класс для тестирования перехода между разделами "Конструктора"
class TestConstruktorSection:

# Тестирование перехода в раздел Соусы
    def test_goto_section_sauces(self,driver):

# Клик по кнопке "Конструктор"

        button_designer=driver.find_element(*BurgerLocators.BTN_DESIGNER)
        button_designer.click()


# Клик по разделу "Соусы"

        btn_ingredients_sauces=driver.find_element(*BurgerLocators.BURGEST_INGRIDIENTS_SAUCES)
        btn_ingredients_sauces.click()


        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.TITLE_SOUSES, 'Соусы'))
        title_souc = driver.find_element(*BurgerLocators.TITLE_SOUSES)

        assert title_souc.is_displayed() and title_souc.text == 'Соусы'

# Тестирование перехода к разделу "Начинки"
    def test_goto_section_fillings(self,driver):

# Клик по кнопке "Конструктор"

        button_designer = driver.find_element(*BurgerLocators.BTN_DESIGNER)
        button_designer.click()

# Клик по разделу Начинки

        btn_ingredients_fillings = driver.find_element(*BurgerLocators.BURGEST_INGRIDIENTS_FILLINGS)
        btn_ingredients_fillings.click()


        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.TITLE_FILLINGS, 'Начинки'))
        title_filling = driver.find_element(*BurgerLocators.TITLE_FILLINGS)

        assert title_filling.is_displayed() and title_filling.text == 'Начинки'


# Тестирование перехода к разделу "Булки"


    def test_goto_section_bulko(self,driver):

# Клик по кнопке "Конструктор"

        button_designer = driver.find_element(*BurgerLocators.BTN_DESIGNER)
        button_designer.click()

# Клик по разделу Начинки

        btn_ingredients_fillings = driver.find_element(*BurgerLocators.BURGEST_INGRIDIENTS_FILLINGS)
        btn_ingredients_fillings.click()


# Клик по разделу Булки
        btn_ingredients_bulko = driver.find_element(*BurgerLocators.BURGEST_INGRIDIENTS_BULKO)
        btn_ingredients_bulko.click()


        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(BurgerLocators.TITLE_BULKO, 'Булки'))
        title_bulko = driver.find_element(*BurgerLocators.TITLE_BULKO)

        assert title_bulko.is_displayed() and title_bulko.text == 'Булки'