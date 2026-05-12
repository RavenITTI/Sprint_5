import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from locators import URLS




class TestConstructor:

    @pytest.mark.parametrize("tab_locator", [
        TestLocators.CONSTRUCTOR_SAUCES_TAB,
        TestLocators.CONSTRUCTOR_FILLINGS_TAB,
        TestLocators.CONSTRUCTOR_BUNS_TAB
    ])
    def test_switch_tabs(self, driver, tab_locator):
        driver.get(URLS.BASE_URL)
        
        if tab_locator == TestLocators.CONSTRUCTOR_BUNS_TAB:
            driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES_TAB).click()
           
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element_attribute(
                    TestLocators.CONSTRUCTOR_SAUCES_TAB, "class", "tab_tab_type_current"
                )
            )

        tab = driver.find_element(*tab_locator)
        tab.click()

       
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                tab_locator, "class", "tab_tab_type_current"
            )
        )

        assert "tab_tab_type_current" in tab.get_attribute("class")