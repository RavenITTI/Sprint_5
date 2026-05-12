import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from locators import URLS



class TestLogin:

    def test_login_from_main_page(self, driver, new_user):
      
        driver.get(URLS.BASE_URL)
        
        driver.find_element(*TestLocators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(new_user["email"])
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(new_user["password"])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.MAIN_ORDER_BUTTON)
        )
        assert driver.find_element(*TestLocators.MAIN_ORDER_BUTTON).is_displayed()



    def test_login_from_profile_button(self, driver, new_user):
        
        driver.get(URLS.BASE_URL)
        
        driver.find_element(*TestLocators.MAIN_PROFILE_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(new_user["email"])
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(new_user["password"])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.MAIN_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.MAIN_ORDER_BUTTON).is_displayed()   
    def test_login_from_registration_form(self, driver, new_user):
      
        driver.get(URLS.REGISTRATION_URL)
        
        driver.find_element(*TestLocators.REG_LOGIN_LINK).click()
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(new_user["email"])
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(new_user["password"])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.MAIN_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.MAIN_ORDER_BUTTON).is_displayed()    
   
   
    def test_login_from_forgot_password_page(self, driver, new_user):
       
        driver.get(f"{URLS.BASE_URL}forgot-password")
        
        driver.find_element(*TestLocators.REG_LOGIN_LINK).click() 
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(new_user["email"])
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(new_user["password"])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.MAIN_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.MAIN_ORDER_BUTTON).is_displayed()