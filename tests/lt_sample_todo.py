import pytest
from selenium.webdriver.common.by import By
import sys
import time


@pytest.mark.usefixtures('driver')
class TestLink:

    def test_title(self, driver):
        driver.maximize_window()
        driver.get('https://dev.bookhive.me/login')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)    
        oldDriver = driver.current_window_handle
        signInButtonToGoogleButton = driver.find_element(By.XPATH, "//div[@class='v-row mt-2']/div/div")
        signInButtonToGoogleButton.click()
        for handle in driver.window_handles:
            if handle != oldDriver:
                login_page = handle
        driver.switch_to.window(login_page) 
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@type='email']").send_keys("testtrt01@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH,"//span[contains(text(),'Next')]//parent::button").click()
        # time.sleep(4)
        # driver.find_element(By.XPATH,"//a[@aria-label='Try again']").click()
        # time.sleep(1)
        # driver.find_element(By.XPATH,"//input[@type='email']").send_keys("atulshworking@gmail.com")
        # time.sleep(1)
        # driver.find_element(By.XPATH,"//span[contains(text(),'Next')]//parent::button").click()
        time.sleep(4)
        driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Effective1?")
        time.sleep(4)
        driver.find_element(By.XPATH,"//span[contains(text(),'Next')]//parent::button").click()
        time.sleep(5)
        driver.close()  
