from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions

def login(self, driver):
    element = WebDriverWait(driver, self.wait_time).until(
        expected_conditions.presence_of_element_located((By.ID, "lnkLogin")))
    driver.find_element_by_link_text("Login").click()

    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("user-name")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("password")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("password")
    driver.find_element_by_id("btnLogin").click()
