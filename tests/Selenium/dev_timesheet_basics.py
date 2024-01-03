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

class TimesheetBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
    
    def test_timesheet_basics(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        login(self, driver)

        driver.maximize_window()

        driver.find_element_by_id("menu-top-time").click()
        driver.find_element_by_id("menu-drop-timesheets").click()

        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "tbTimeSheet"))
        )

        driver.find_element_by_id("frmDatePicker").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_class_name("ui-datepicker-prev").click()
        driver.find_element_by_class_name("ui-datepicker-prev").click()
        driver.find_element_by_class_name("ui-datepicker-prev").click()

        driver.find_element_by_link_text("1").click()
        sleep(self.test.sleep_time)

        dp2 = driver.find_element_by_id("frmDatePicker2").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_link_text("28").click()

        driver.find_element_by_id("btn-timesheet").click()

        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "tbTimeSheet"))
        )

        # Log out
        driver.find_element_by_id("lnkAdminMenu").click()
        driver.find_element_by_id("logout").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
