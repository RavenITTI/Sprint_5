import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from helpers import generate_user_data


def test_successful_registration(driver):
    user = generate_user_data()
    driver.find_element(*TestLocators.MAIN_LOGIN_BUTTON).click()  
    driver.find_element(*TestLocators.LOGIN_REGISTER_LINK).click()  
    
    driver.find_element(*TestLocators.REG_NAME).send_keys(user["name"]) 
    driver.find_element(*TestLocators.REG_EMAIL).send_keys(user["email"]) 
    driver.find_element(*TestLocators.REG_PASSWORD).send_keys(user["password"])  
   
    driver.find_element(*TestLocators.REG_BUTTON).click()  

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON))
    
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"  



def test_registration_short_password_error(driver):
    user = generate_user_data()

    driver.find_element(*TestLocators.MAIN_LOGIN_BUTTON).click()
    driver.find_element(*TestLocators.LOGIN_REGISTER_LINK).click()

    driver.find_element(*TestLocators.REG_NAME).send_keys(user["name"])
    driver.find_element(*TestLocators.REG_EMAIL).send_keys(user["email"])
    driver.find_element(*TestLocators.REG_PASSWORD).send_keys("12345") 
        
    driver.find_element(*TestLocators.REG_BUTTON).click()

    
    error_message = driver.find_element(*TestLocators.REG_ERROR)
    assert error_message.is_displayed()
    assert error_message.text == "Некорректный пароль"