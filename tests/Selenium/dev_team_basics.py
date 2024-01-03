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
from tests.Selenium.functions.logout import logout

class TeamBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
    
    def test_team_basics(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        login(self, driver)

        driver.maximize_window()

        sleep(self.test.sleep_time)

        self.wait_for_element_clickable("menu-top-people")
        driver.find_element_by_id("menu-top-people").click()
        self.wait_for_element_clickable("menu-drop-team-create")
        driver.find_element_by_id("menu-drop-team-create").click()

        # Create team
        self.wait_for_element_clickable("btn-team-create")
        driver.find_element_by_id("frmTeamName").clear()
        driver.find_element_by_id("frmTeamName").send_keys("Test team")
        driver.find_element_by_id("frmTeamDescription").clear()
        driver.find_element_by_id("frmTeamDescription").send_keys("Test team")
        driver.find_element_by_id("btn-team-create").click()

        sleep(self.test.sleep_time)

        # Edit team
        self.wait_for_element_clickable("lnkEditTeam")
        driver.find_element_by_link_text("Edit Team").click()
        driver.find_element_by_id("frmTeamDescription").clear()
        driver.find_element_by_id("frmTeamDescription").send_keys("Test team changed")
        driver.find_element_by_id("btn-team-edit").click()

        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Team Overview"))
        )

        # Log out
        logout(self, driver)
    
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
