from selenium.webdriver.common.by import By



class TestLocators:
# Групаа лакаторов для регистрации
  REG_NAME=(By.XPATH, ".//fieldset[1]//input")
  REG_EMAIL=(By.XPATH, ".//fieldset[2]//input")
  REG_PASSWORD=(By.XPATH, ".//input[@type='password']")
  REG_BUTTON=(By.XPATH, ".//button[text()='Зарегистрироваться']")
  REG_ERROR=(By.XPATH, ".//p[contains(@class, 'input__error')]")
  REG_LOGIN_LINK=(By.XPATH, ".//a[@href='/login']") # Ссылка на страницу входа
  
#  Группа лакаторов для входа 
  LOGIN_EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
  LOGIN_PASSWORD_FIELD =(By.XPATH, ".//input[@name='Пароль']")
  LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
  LOGIN_REGISTER_LINK = (By.XPATH, ".//a[@href='/register']") # Ссылка на страницу регистрации
  LOGIN_FORGOT_PASSWORD_LINK= (By.XPATH, ".//a[@href='/forgot-password']") # Ссылка на страницу восстановления пароля

#  Группа лакаторов для главной страницы
  MAIN_LOGIN_BUTTON =(By.XPATH, ".//button[text()='Войти в аккаунт']")
  MAIN_PROFILE_BUTTON =(By.XPATH,  ".//a[@href='/account']")
  MAIN_CONSTRUCTOR_LINK =(By.XPATH, ".//p[text()='Конструктор']/parent::a")
  MAIN_LOGO =(By.XPATH, ".//div[contains(@class, 'logo')]/a")
  MAIN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

# Группа лакаторов для конструктора
  CONSTRUCTOR_BUNS_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab')][span[text()='Булки']]")
  CONSTRUCTOR_SAUCES_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab')][span[text()='Соусы']]")
  CONSTRUCTOR_FILLINGS_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab')][span[text()='Начинки']]")

# Группа лакаторов для профиля
  PROFILE_LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
  PROFILE_INFO_TEXT = (By.XPATH, ".//p[contains(text(), 'изменить свои персональные данные')]")
