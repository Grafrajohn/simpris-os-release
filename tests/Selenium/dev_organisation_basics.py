# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest, time, re
from time import sleep
from tests.Selenium.functions.properties_test import TestProperties
from tests.Selenium.functions.login import login

class OrganisationBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
    
    def test_organisation_basics(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        login(self, driver)

        driver.maximize_window()

        sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-top-people")))

        # menu
        driver.find_element_by_id("menu-top-people").click()
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-drop-clients")))
        driver.find_element_by_id("menu-drop-clients").click()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "tbOrganisationIndex")))

        driver.find_element_by_id("menu-top-people").click()
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-drop-organisation")))
        driver.find_element_by_id("menu-drop-organisation").click()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "frmOrganisationName")))

        # add organisation
        driver.find_element_by_id("frmOrganisationName").clear()
        driver.find_element_by_id("frmOrganisationName").send_keys("Test Organisation " + self.current_date_time)
        driver.find_element_by_id("btn-organisation-create").click()

        # visit history
        driver.find_element_by_link_text("Organisation History").click()
        sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "divOrganisationHistory")))

        # edit organisation
        driver.find_element_by_link_text("Edit Organisation").click()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "frmOrganisationEdit")))

        driver.find_element_by_id("frmOrganisationName").clear()
        driver.find_element_by_id("frmOrganisationName").send_keys("Test Organisation changed" + self.current_date_time)
        driver.find_element_by_id("btn-organisation-edit").click()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Organisation Overview")))

        # visit overview
        driver.find_element_by_link_text("Organisation Overview").click()

        #element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "divOrganisationOverview")))
        time.sleep(self.test.sleep_time)

        # log out
        driver.find_element_by_css_selector("#lnkAdminMenu > b.caret").click()
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "logout")))
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
