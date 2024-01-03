import unittest, time, re
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions

def logout(self, driver):
    driver.find_element_by_css_selector("#lnkAdminMenu > b.caret").click()
    element = WebDriverWait(driver, self.wait_time).until(
        EC.visibility_of_element_located((By.ID, "logout"))
    )
    sleep(self.test.sleep_time)
    driver.find_element_by_id("logout").click()