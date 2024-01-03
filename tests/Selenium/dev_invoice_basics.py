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

class InvoiceBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.base_url = self.test.base_url
        self.driver.implicitly_wait(self.test.wait_time)
        self.current_date_time = self.test.test_time
        self.verificationErrors = []
        self.accept_next_alert = True
        self.wait_time = self.test.wait_time
    
    def test_invoice_basics(self):
        driver = self.driver
        self.test.maximise_window()
        driver.get(self.base_url + "/")

        login(self, driver)

        sleep(self.test.sleep_time)

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-top-time")))

        driver.find_element_by_id("menu-top-time").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_id("menu-drop-invoice").click()
        sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "btn-invoice-create")))
        driver.find_element_by_id("btn-invoice-create").click()
        sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "btn-invoice-create")))

        # add invoice details
        driver.find_element_by_id("frmDatePicker").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("frmDescription").clear()
        driver.find_element_by_name("frmDescription").send_keys("Description")
        sleep(self.test.sleep_time)
        driver.find_element_by_id("frmDatePicker2").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_link_text("28").click()
        driver.find_element_by_name("frmComments").clear()
        driver.find_element_by_name("frmComments").send_keys("Comments")

        # create invoice
        driver.find_element_by_id("btn-invoice-create").click()

        # wait for element
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "btn-add-invoice-tasks")))

        # find invoice
        driver.find_element_by_name("timeID[]").click()
        driver.find_element_by_xpath("(//input[@name='timeID[]'])[2]").click()
        driver.find_element_by_xpath("(//input[@name='timeID[]'])[3]").click()
        driver.find_element_by_xpath("(//input[@name='timeID[]'])[4]").click()

        # add items to invoice
        driver.find_element_by_id("btn-add-invoice-tasks").click()

        # wait for element
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "lnkInvoicePrint")))

        # log off
        driver.find_element_by_css_selector("#lnkAdminMenu > b.caret").click()
        sleep(self.test.sleep_time)
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
