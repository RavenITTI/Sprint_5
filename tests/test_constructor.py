import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators





# 2 Теста сделал так чтобы было визуально видно, что вкладка действительно переключается (вывод класса до и после клика)
class TestConstructor:

    def test_go_to_sauces_tab(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        
        tab = driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES_TAB)
        
       
        print(f"\nКласс до клика: {tab.get_attribute('class')}")
        
        tab.click()
        
       
        time.sleep(1) 
        
        
        print(f"Класс после клика: {tab.get_attribute('class')}")
        
        assert "current" in tab.get_attribute("class")

    def test_go_to_fillings_tab(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        
        
        tab = driver.find_element(*TestLocators.CONSTRUCTOR_FILLINGS_TAB)
        
        
        print(f"\n[Начинки] Класс до клика: {tab.get_attribute('class')}")
        
        
        tab.click()
        
       
        time.sleep(1) 
        
        
        current_class = tab.get_attribute('class')
        print(f"[Начинки] Класс после клика: {current_class}")
        
        
        assert "tab_tab_type_current" in current_class
    def test_go_to_buns_tab(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        
       
        driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES_TAB).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUNS_TAB).click()
        
        tab_class = driver.find_element(*TestLocators.CONSTRUCTOR_BUNS_TAB).get_attribute("class")
        
        assert "tab_tab_type_current" in tab_class