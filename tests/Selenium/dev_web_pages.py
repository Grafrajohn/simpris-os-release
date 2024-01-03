# -*- coding: utf-8 -*-
import unittest, time, re
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from tests.Selenium.functions.properties_test import TestProperties

class WebPages(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.base_url = self.test.base_url
        self.driver.implicitly_wait(self.test.wait_time)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_web_pages(self):
        driver = self.driver
        driver.get(self.base_url)
        # Features page
        driver.find_element_by_link_text("Features").click()
        src = driver.page_source
        text_found = re.search(r'Other Features', src)
        self.assertNotEqual(text_found, None)
        # Tour page
        driver.find_element_by_link_text("Tour").click()
        src = driver.page_source
        text_found = re.search(r'Your time and your resources = your money', src)
        self.assertNotEqual(text_found, None)
        # Pricing page
        driver.find_element_by_link_text("Pricing / Sign Up").click()
        src = driver.page_source
        text_found = re.search(r'Pricing / Sign Up', src)
        self.assertNotEqual(text_found, None)
        # About page
        driver.find_element_by_link_text("About Us").click()
        src = driver.page_source
        text_found = re.search(r'The Simpris Team', src)
        self.assertNotEqual(text_found, None)
        # Contact page
        driver.find_element_by_link_text("Contact Us").click()
        src = driver.page_source
        text_found = re.search(r'Contact Details', src)
        self.assertNotEqual(text_found, None)
        # Support page
        driver.find_element_by_link_text("Support").click()
        src = driver.page_source
        text_found = re.search(r'The support our customers need', src)
        self.assertNotEqual(text_found, None)
        # Login page
        driver.find_element_by_link_text("Login").click()
        src = driver.page_source
        elem = driver.find_element_by_id('btnLogin')
        self.assertNotEqual(elem, None)
    
    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException, e: return False
    #     return True
    #
    # def is_alert_present(self):
    #     try: self.driver.switch_to_alert()
    #     except NoAlertPresentException, e: return False
    #     return True
    
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
