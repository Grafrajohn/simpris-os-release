'''
Created on 27 Jun 2015

Log in and log out

@author: Graham
'''
import unittest, time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from simpris.settings import BASE_URL_CI

from tests.Selenium.functions.properties_test import TestProperties

class SimprisLoginLogout(unittest.TestCase, TestProperties):

    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url


    def test_login_logoff(self):
        # set variables here
        startsite = self.base_url
        URL = startsite + "/auth/logon"

        self.driver.get(URL)

        self.test.maximise_window()

        # wait until page loads
        WebDriverWait(self.driver, self.test.wait_time).until(
            EC.title_contains("Simpris"
            )
        )
        assert "Simpris" in self.driver.title

        # complete login form
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(self.test.username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(self.test.password)

        # press button to log in
        self.driver.find_element_by_id('btnLogin').click()

        # wait until page loads
        WebDriverWait(self.driver, self.test.wait_time).until(
            EC.title_contains("Simpris"
            )
        )

        h3 = self.driver.find_element_by_class_name('indexPageHeader')
        assert "Critical work across all my projects" in h3.text

        self.driver.find_element_by_id("lnkAdminMenu").click()

        sleep(self.test.sleep_time)

        # wait until page loads
        WebDriverWait(self.driver, self.test.wait_time).until(
            EC.element_to_be_clickable((By.ID, "logout"))
        )

        # click on logout
        self.driver.find_element_by_id("logout").click()

        # wait until page loads
        WebDriverWait(self.driver, self.test.wait_time).until(
            EC.presence_of_element_located((By.ID, "loginHeader"))
        )

        # check that we are back at login page
        h3 = self.driver.find_element_by_id("loginHeader")
        assert "Login" in h3.text


    def tearDown(self):
        self.driver.close()
