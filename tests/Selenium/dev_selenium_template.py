# -*- coding: utf-8 -*-
import unittest, time, re
from time import sleep

# selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tests.Selenium.functions.properties_test import TestProperties
from tests.Selenium.functions.login import login, logout

class XXXBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        test_properties = TestProperties()
        self.driver = self.test.driver

        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
    
    def test_xxx_basics(self):

        driver = self.driver
        driver.get(self.base_url + "/")

        # login
        login(self, driver)

        driver.maximize_window()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-top-project")))

        # menu
        driver.find_element_by_id("menu-top-xxx").click()
        driver.find_element_by_id("menu-drop-xxx").click()
        driver.find_element_by_id("menu-top-xxx").click()
        driver.find_element_by_id("menu-drop-xxx").click()

        # form complete
        driver.find_element_by_id("frmXXXName").clear()
        driver.find_element_by_id("frmXXXName").send_keys("Test Organisation " + self.current_date_time)
        driver.find_element_by_id("btn-xxx-create").click()

        # history
        driver.find_element_by_link_text("XXX History").click()

        # form edit
        driver.find_element_by_link_text("Edit XXX").click()
        driver.find_element_by_id("frmXXXName").clear()
        driver.find_element_by_id("frmXXXName").send_keys("Test Organisation changed" + self.current_date_time)
        driver.find_element_by_id("btn-xxx-edit").click()

        # overview
        driver.find_element_by_link_text("XXX Overview").click()

        # logout
        logout(self, driver)
    
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
