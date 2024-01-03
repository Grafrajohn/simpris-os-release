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

class ScheduleBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
    
    def test_schedule_basics(self):
        driver = self.driver

        driver.get(self.base_url + "/")

        login(self, driver)

        driver.maximize_window()
        sleep(self.test.sleep_time)

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-top-time")))

        # visit calendar
        driver.find_element_by_id("menu-top-time").click()
        sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(
            expected_conditions.visibility_of_element_located((By.ID, "menu-drop-schedule"))
        )
        sleep(self.test.sleep_time)
        driver.find_element_by_id("menu-drop-schedule").click()
        sleep(self.test.sleep_time)

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "txtTask")))

        # task search form complete
        driver.find_element_by_id("txtTask").clear()
        driver.find_element_by_id("txtTask").send_keys("Simpris")
        driver.find_element_by_id("txtTask").click()

        sleep(self.test.sleep_time)

        # pick schedule item
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "schedule-list-item")))
        element_source = driver.find_element_by_class_name('schedule-list-item')
        element_dest = driver.find_element_by_id('schedule-list-3')
        self.test.drag_and_drop_elements(element_source, element_dest)

        # find moved task in destination list
        self.test.find_item_in_list('schedule-list-3', element_source.text, 'li')

        # logout
        driver.find_element_by_css_selector("#lnkAdminMenu > b.caret").click()
        element = WebDriverWait(driver, self.wait_time).until(
            expected_conditions.visibility_of_element_located((By.ID, "logout"))
        )
        sleep(self.test.sleep_time)
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
