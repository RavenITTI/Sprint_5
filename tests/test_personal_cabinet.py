import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from locators import URLS


class TestPersonalCabinet:

    #  Переход в личный кабинет
    def test_go_to_personal_cabinet(self, driver, authorized_user):
        driver.find_element(*TestLocators.MAIN_PROFILE_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.PROFILE_INFO_TEXT)
        )
        assert driver.find_element(*TestLocators.PROFILE_INFO_TEXT).is_displayed()


    # Переход из личного кабинета в конструктор по клику на «Конструктор»
    def test_go_from_cabinet_to_constructor(self, driver, authorized_user):
        driver.find_element(*TestLocators.MAIN_PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.MAIN_CONSTRUCTOR_LINK))
        driver.find_element(*TestLocators.MAIN_CONSTRUCTOR_LINK).click()
        assert driver.find_element(*TestLocators.MAIN_ORDER_BUTTON).is_displayed()



    #  Переход из личного кабинета в конструктор по клику на Логотип
    def test_go_from_cabinet_to_constructor_via_logo(self, driver, authorized_user):
        driver.find_element(*TestLocators.MAIN_PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.MAIN_LOGO))
        driver.find_element(*TestLocators.MAIN_LOGO).click()
        assert driver.find_element(*TestLocators.MAIN_ORDER_BUTTON).is_displayed()



    # Выход из аккаунта
    def test_logout(self, driver, authorized_user):
        driver.find_element(*TestLocators.MAIN_PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.PROFILE_LOGOUT_BUTTON))
        driver.find_element(*TestLocators.PROFILE_LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        assert driver.current_url == URLS.LOGIN_URL