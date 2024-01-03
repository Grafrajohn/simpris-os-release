# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from tests.Selenium.functions.properties_test import TestProperties


class LiveQuickLook(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_live_quick_look(self):
        driver = self.driver
        driver.get(self.test.live_base_url)
        driver.find_element_by_link_text("Features").click()
        driver.find_element_by_link_text("Tour").click()
        driver.find_element_by_link_text("Pricing / Sign Up").click()
        driver.find_element_by_link_text("About Us").click()
        driver.find_element_by_link_text("Contact Us").click()
        driver.find_element_by_link_text("Support").click()
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("user-name")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("password")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_id("menu-top-project").click()
        driver.find_element_by_id("menu-drop-projects").click()
        driver.find_element_by_css_selector("i.fa.fa-user").click()
        dropdown = driver.find_element_by_id("lnkAdminMenu")
        # dropdown = self.driver.find_element_by_id('lnkAdminMenu')
        dropdown.click()
        # click on logout
        logout = driver.find_element_by_id("logout")
        logout.click()
    
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
