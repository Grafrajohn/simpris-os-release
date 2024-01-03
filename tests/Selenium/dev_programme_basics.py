# -*- coding: utf-8 -*-
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

class ProgrammeBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
    
    def test_programme_basics(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        login(self, driver)

        driver.maximize_window()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-top-project")))

        # visit programme list
        driver.find_element_by_id("menu-top-project").click()
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-drop-programmes")))
        driver.find_element_by_id("menu-drop-programmes").click()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-top-project")))
        sleep(self.test.sleep_time)

        # create programme
        driver.find_element_by_id("menu-top-project").click()
        driver.find_element_by_id("menu-drop-programme-create").click()
        driver.find_element_by_id("frmProgrammeName").clear()
        driver.find_element_by_id("frmProgrammeName").send_keys("Test programme " + self.current_date_time)
        driver.find_element_by_id("frmProgrammeDescription").clear()
        driver.find_element_by_id("frmProgrammeDescription").send_keys("Test programme")
        driver.find_element_by_id("btn-programme-create").click()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Edit Programme")))

        # edit programme
        driver.find_element_by_link_text("Edit Programme").click()
        driver.find_element_by_id("frmProgrammeDescription").send_keys("Test programme edited here")
        driver.find_element_by_id("btn-programme-edit").click()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Programme History")))

        # visit history
        driver.find_element_by_link_text("Programme History").click

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Programme Overview")))

        # visit overview
        driver.find_element_by_link_text("Programme Overview").click()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "lnkAdminMenu")))

        # log out
        driver.find_element_by_css_selector("#lnkAdminMenu > b.caret").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_id("logout").click()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
