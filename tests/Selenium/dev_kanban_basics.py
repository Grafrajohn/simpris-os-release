import unittest, time, re
from time import sleep

# selenium imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# tests imports
from tests.Selenium.functions.properties_test import TestProperties
from tests.Selenium.functions.login import login


class KanbanBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver

        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
    
    def test_kanban_basics(self):

        driver = self.driver
        driver.get(self.base_url + "/")

        # login
        login(self, driver)

        driver.maximize_window()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-top-time")))

        # menu
        driver.find_element_by_id("menu-top-time").click()
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-drop-kanban")))
        sleep(self.test.sleep_time)
        driver.find_element_by_id("menu-drop-kanban").click()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "kanban-item")))

        # logout
        driver.find_element_by_css_selector("#lnkAdminMenu > b.caret").click()
        time.sleep(2)
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.presence_of_element_located((By.ID, "logout")))
        driver.find_element_by_id("logout").click()
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
