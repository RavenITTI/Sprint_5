import pytest
from selenium import webdriver 
from helpers import generate_user_data
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture
def driver():
    # Создаем браузер
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(16)
    
    browser.get("https://stellarburgers.education-services.ru")
    
    yield browser 
    
    browser.quit()
@pytest.fixture
def new_user(driver):
    """ Для создания нового пользователя перед тестами входа."""
    user_data = generate_user_data()

  
    driver.get("https://stellarburgers.education-services.ru/register")
    driver.find_element(*TestLocators.REG_NAME).send_keys(user_data["name"])
    driver.find_element(*TestLocators.REG_EMAIL).send_keys(user_data["email"])
    driver.find_element(*TestLocators.REG_PASSWORD).send_keys(user_data["password"])
    driver.find_element(*TestLocators.REG_BUTTON).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
    
    return user_data 
@pytest.fixture
def authorized_user(driver, new_user):
    """Регистрирует и сразу логинит пользователя."""
    driver.get("https://stellarburgers.education-services.ru/login")
    driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(new_user["email"])
    driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(new_user["password"])
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    
    # Ждем, когда вход завершится (появится кнопка заказа)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.MAIN_ORDER_BUTTON))
    
    return new_user