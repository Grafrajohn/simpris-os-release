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

class Register(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.base_url = self.test.base_url
        self.driver.implicitly_wait(self.test.wait_time)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
    
    def test_register(self):
        driver = self.driver
        driver.get(self.base_url + "/register/new")

        current_date_time = time.strftime('%Y-%m-%d-%H-%M-%S')
        test_company = "Test-Company-" + current_date_time
        test_surname = "Test-" + current_date_time

        driver.maximize_window()

        # populate registration form
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "frmRegister")))
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("William")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys(test_surname)
        driver.find_element_by_id("company").clear()
        driver.find_element_by_id("company").send_keys(test_company)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("testcompany_" + current_date_time + "@simpris.com")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("0123412345678")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("William-" + current_date_time)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("password")
        driver.find_element_by_id("password_confirm").clear()
        driver.find_element_by_id("password_confirm").send_keys("password")
        driver.find_element_by_id("tcs").click()

        # submit registration form
        driver.find_element_by_xpath("//input[@value='Create your account']").click()

        sleep(self.test.sleep_time)

        # check post-registration setup
        driver.find_element_by_id("menu-top-project").click()
        # count project rows
        driver.find_element_by_link_text("My Projects").click()
        row_count = len(driver.find_elements_by_xpath("//table[@id='tbProjectIndex']/tbody/tr"))
        self.assertEquals(row_count, 1)

        # count problem rows
        driver.find_element_by_id("menu-top-problems").click()
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "My Problems")))
        driver.find_element_by_link_text("My Problems").click()
        row_count = len(driver.find_elements_by_xpath("//table[@id='tbProblemIndex']/tbody/tr"))
        self.assertEquals(row_count, 1)

        # count people rows
        driver.find_element_by_id("menu-top-people").click()
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-drop-people")))
        driver.find_element_by_id("menu-drop-people").click()
        row_count = len(driver.find_elements_by_xpath("//table[@id='tbUserIndex']/tbody/tr"))
        self.assertEquals(row_count, 1)
        elem = driver.find_element_by_xpath("//table[@id='tbUserIndex'][contains(text(), " + test_surname + ")]")
        self.assertTrue(len(elem.text) > 0)

        # count clients
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-top-people")))
        driver.find_element_by_id("menu-top-people").click()
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-drop-clients")))
        driver.find_element_by_id("menu-drop-clients").click()
        row_count = len(driver.find_elements_by_xpath("//table[@id='tbOrganisationIndex']/tbody/tr"))
        self.assertEquals(row_count, 1)
        elem2 = driver.find_element_by_xpath("//table[@id='tbOrganisationIndex'][contains(text(), " + test_company + ")]")
        self.assertTrue(len(elem2.text) > 0)

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-top-time")))
        driver.find_element_by_id("menu-top-time").click()
        #driver.find_element_by_id("content-wrapper").click()

        # logout
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "lnkAdminMenu")))
        driver.find_element_by_id("lnkAdminMenu").click()
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
