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
from tests.Selenium.functions.login import login
from tests.Selenium.functions.logout import logout

class TimeGridBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver

        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
    
    def test_timegrid_basics(self):

        driver = self.driver
        driver.get(self.base_url + "/")

        # login
        login(self, driver)

        driver.maximize_window()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-top-time")))

        # menu
        driver.find_element_by_id("menu-top-time").click()
        driver.find_element_by_id("menu-drop-time-edit").click()

        # date picker
        driver.find_element_by_id("frmDatePicker").click()
        driver.find_element_by_class_name("ui-state-active").click()

        # choose task to add time to
        Select(driver.find_element_by_id("selTask")).select_by_index(1)
        select = Select(driver.find_element_by_id('selTask'))
        selected_option = select.first_selected_option.text

        # choose start time
        Select(driver.find_element_by_id("selStartHour")).select_by_index(10)
        Select(driver.find_element_by_id("selStartMins")).select_by_index(2)

        # choose end time
        Select(driver.find_element_by_id("selDurationHours")).select_by_index(1)
        Select(driver.find_element_by_id("selDurationMins")).select_by_index(2)

        # create time
        driver.find_element_by_id("butInsert").click()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "tabTimes")))

        # refresh page
        driver.refresh()

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "tabTimes")))

        # check task time
        table = driver.find_element_by_id("tabTimes")
        time_task_found = False
        for cell in table.find_elements_by_tag_name("td"):
            if cell.text in selected_option:
                time_task_found = True
        assert (time_task_found == True), selected_option

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
