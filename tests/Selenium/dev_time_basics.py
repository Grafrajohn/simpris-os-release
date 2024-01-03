# -*- coding: utf-8 -*-
import unittest, time, re
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.Selenium.functions.properties_test import TestProperties
from tests.Selenium.functions.login import login

class TimeBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.base_url = self.test.base_url
        self.driver.implicitly_wait(self.test.wait_time)
        self.current_date_time = self.test.test_time
        self.verificationErrors = []
        self.accept_next_alert = True
        self.wait_time = self.test.wait_time
    
    def test_time_basics(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url + "/")

        login(self, driver)

        # time index
        driver.find_element_by_id("menu-top-time").click()
        #driver.find_element_by_id("menu-drop-times").click()
        #driver.find_element_by_xpath("//header[@id='header-navbar']/div/div/div/ul/li[5]/a/b").click()

        # add time
        driver.find_element_by_id("menu-drop-time-create").click()
        #driver.find_element_by_link_text("Add time").click()
        driver.find_element_by_id("frmDatePicker").click()
        driver.find_element_by_link_text("28").click()
        Select(driver.find_element_by_id("frmHours")).select_by_visible_text("02")
        Select(driver.find_element_by_id("frmMins")).select_by_visible_text("15")
        Select(driver.find_element_by_id("frmTaskID")).select_by_index(1)
        Select(driver.find_element_by_id("frmTimeType")).select_by_visible_text("Agree scope")
        driver.find_element_by_name("frmComments").clear()
        driver.find_element_by_name("frmComments").send_keys("Comment here")
        driver.find_element_by_id("btn-time-create").click()

        # click around new time
        driver.find_element_by_link_text("Edit Time").click()
        driver.find_element_by_link_text("Time Detail").click()

        # change comment
        driver.find_element_by_link_text("Edit Time").click()
        driver.find_element_by_id("frmComment").clear()
        driver.find_element_by_id("frmComment").send_keys("Comment here again.")
        driver.find_element_by_id("btn-time-edit").click()

        sleep(self.test.sleep_time)

        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Time Detail"))
        )

        driver.find_element_by_link_text("Time Detail").click()

        # logout
        driver.find_element_by_id("lnkAdminMenu").click()
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
