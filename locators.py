from selenium.webdriver.common.by import By

# Локаторы главной страницы:
class  BurgerLocators:
    # Заголовок Рестрация
    REGISTRATION_TITLE = (By.XPATH,"//h2[text()='Регистрация']")

    # Заголовок формы  входа "Личный кабинет" и "Войти в аккаунт"
    REGISTRATION_TITLE_PERSONAL_ACCOUNT = (By.XPATH ,"//h2[text()='Вход']")

    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_SUBMIT_MAIN = (By.XPATH, "//button[text() = 'Войти в аккаунт']")

    # Кнопка "Личный кабинет" на главной странице
    LOGIN_SUBMIT_PERSONAL_ACCOUNT = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href ='/account']")

    # Раздел булки
    BURGEST_INGRIDIENTS_BULKO = (By.XPATH, "//span[text()='Булки']")

    # Раздел соусы
    BURGEST_INGRIDIENTS_SAUCES = (By.XPATH, "//span[text()='Соусы']")

    # Раздел начинки
    BURGEST_INGRIDIENTS_FILLINGS = (By.XPATH, "//span[text()='Начинки']")

    # кнопка "Конструктор"
    BTN_DESIGNER = (By.XPATH, "//*[@class='AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo']")

    # Заголовок Собери бургер на главной странице
    TITLE_COLLECT_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")

    # Кнопка Оформить заказ
    BTN_PLACE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")

    # Поле "Имя" в форме Регистрация
    LOGIN_NAME_INPUT = (By.XPATH,'.//label[text()="Имя"]/parent::div/input')

    # Поле "Email"
    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::*")

    # Поле " Пароль"
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    # Кнопка "Зарегестрироваться" в форме "Регистрация"
    LOGIN_SUBMIT = (By.XPATH, "//button[text() = 'Зарегистрироваться']")

    # Кнопка "Войти" в форме "Личный кабинет" и "Войти в аккаунт"
    LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

    # Ссылка "Зарагестрироваться"
    LOGIN_SUBMIT_REGISTER= (By.XPATH,"//a[@href='/register']")

    # Ссылка "Восстановить пароль"
    LOGIN_SUBMIT_RECOVER_PASSWORD = (By.XPATH,"//a[@href='/forgot-password']")

    # Кнопка войти в форме "Восстановить пароль"
    LOGIN_SUBMIT_PERSONAL_ACCOUNT_BUTTON_PASSWORD= (By.XPATH, "// *[ @ href = '/login']")

    # Кнопка "конструктор" В Личном кабинете
    BTN_DESIGNER_TWO =(By.XPATH ," // *[ @class ='undefined ml-2'] / preceding-sibling::*")

    # Надпись Stellar Burgers в Личном кабинете
    CLICK_IN_STELLAR_BYRGERS_TWO = (By.XPATH,"//*[@fill='none']")

    # надпись Stellar Burgers
    CLICK_IN_STELLAR_BYRGERS = (By.XPATH,"//*[@aria-current='page' and @class='active']")

    # кнопка "Выход" в "Личном кабинете"
    BTN_EXIT_ON_PERSONAL_ACCOUNT = (By.XPATH , "//button[text()='Выход']")

    # Надпись Профиль в Личном кабинете
    TITLE_PROFILE = (By.XPATH , "//*[@href='/account/profile']")

    # сообщение "Некорректный пароль"
    INCORRECT_PASSWORD_MSG = (By.XPATH, './/p[text()="Некорректный пароль"]')

    # Заголовок Соусы в конструкторе
    TITLE_SOUSES = (By.XPATH , './/span[text() = "Соусы"]')

    # Заголовок Булки в конструкторе
    TITLE_BULKO = (By.XPATH , './/h2[text() = "Булки"]')

    # Заголовок Начинки в конструкторе
    TITLE_FILLINGS = (By.XPATH , './/h2[text() = "Начинки"]')



