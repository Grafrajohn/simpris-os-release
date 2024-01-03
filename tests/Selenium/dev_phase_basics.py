# -*- coding: utf-8 -*-
import unittest, time, re
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from tests.Selenium.functions.properties_test import TestProperties
from tests.Selenium.functions.login import login

class PhaseBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        #self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
    
    def test_phase_basics(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        login(self, driver)

        driver.maximize_window()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-top-time")))

        driver.find_element_by_id("menu-top-time").click()
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-drop-phase")))
        driver.find_element_by_id("menu-drop-phase").click()
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "tbPhaseIndex")))
        driver.find_element_by_class_name("fa-edit").click()

        # Edit phase
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "btn-phase-edit")))
        driver.find_element_by_id("frmPhaseDescription").clear()
        driver.find_element_by_id("frmPhaseDescription").send_keys("Phase 1 desc here test")
        driver.find_element_by_id("btn-phase-edit").click()

        time.sleep(self.test.sleep_time)

        # find menu to create phase
        driver.find_element_by_css_selector("#lnkAdminMenu > b.caret").click()
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "lnkPhaseCreate")))
        driver.find_element_by_id("lnkPhaseCreate").click()

        time.sleep(self.test.sleep_time)

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "frmPhaseName")))

        # Enter details of new phase
        driver.find_element_by_id("frmPhaseName").clear()
        driver.find_element_by_id("frmPhaseName").send_keys(self.test.test_time)

        driver.find_element_by_id("frmPhaseDescription").clear()
        driver.find_element_by_id("frmPhaseDescription").send_keys(self.test.test_time)
        driver.find_element_by_id("frmDatePicker2").click()
        driver.find_element_by_link_text("28").click()
        time.sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.visibility_of_element_located((By.ID, "frmDatePicker2")))
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "frmDatePicker2")))
        driver.find_element_by_id("frmDatePicker").click()
        driver.find_element_by_link_text("1").click()
        time.sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "btn-phase-create")))
        driver.find_element_by_id("btn-phase-create").click()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.presence_of_element_located((By.ID, "divPhaseDetail")))

        # Edit phase
        driver.find_element_by_link_text("Edit Phase").click()
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "btn-phase-edit")))
        driver.find_element_by_id("frmPhaseDescription").clear()
        driver.find_element_by_id("frmPhaseDescription").send_keys("Test phase changed")
        driver.find_element_by_id("frmDatePicker").click()
        driver.find_element_by_link_text("2").click()
        time.sleep(self.test.sleep_time)
        driver.find_element_by_id("frmDatePicker2").click()

        driver.find_element_by_link_text("27").click()
        time.sleep(self.test.sleep_time)
        driver.find_element_by_id("btn-phase-edit").click()

        WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "btn-phase-edit")))
        sleep(self.test.sleep_time)

        # View phase overview
        driver.find_element_by_link_text("Phase Overview").click()
        # driver.find_element_by_id("menu_drop_phase").click()
        # Logout
        sleep(self.test.sleep_time)
        driver.find_element_by_id("lnkAdminMenu").click()
        sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "logout")))
        driver.find_element_by_id("logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
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
