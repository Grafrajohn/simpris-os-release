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
from selenium.webdriver.support import expected_conditions

from tests.Selenium.functions.properties_test import TestProperties
from tests.Selenium.functions.login import login

class ProblemBasics(unittest.TestCase):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
    
    def test_problem_basics(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        login(self, driver)

        driver.maximize_window()

        element = WebDriverWait(driver, self.wait_time).until(
            EC.element_to_be_clickable((By.ID, "menu-top-people"))
        )

        # Add organisation
        driver.find_element_by_id("menu-top-people").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_id("menu-drop-organisation").click()
        sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(
            EC.element_to_be_clickable((By.ID, "frmOrganisationAdd"))
        )
        driver.find_element_by_id("frmOrganisationName").clear()
        driver.find_element_by_id("frmOrganisationName").send_keys("Test Organisation " + self.current_date_time)
        driver.find_element_by_id("btn-organisation-create").click()

        sleep(self.test.sleep_time)
        # view the organisation
        driver.find_element_by_link_text("Organisation History").click()
        element = WebDriverWait(driver, self.wait_time).until(
            expected_conditions.presence_of_element_located((By.ID, "footer-copyright")))
        sleep(self.test.sleep_time)
        driver.find_element_by_link_text("Organisation Overview").click()

        sleep(self.test.sleep_time)
        # Add problem
        driver.find_element_by_id("menu-top-problems").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_id("menu-drop-problem-create").click()
        sleep(self.test.sleep_time)
        # wait for element
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "frmOrganisation")))
        Select(driver.find_element_by_id("frmOrganisation")).select_by_visible_text("Test Organisation " + self.current_date_time)
        sleep(self.test.sleep_time)
        driver.find_element_by_id("frmProblemHeader").clear()
        driver.find_element_by_id("frmProblemHeader").send_keys("Test organisation problem " + self.current_date_time)
        sleep(self.test.sleep_time)
        driver.find_element_by_id("frmProblemDescription").clear()
        driver.find_element_by_id("frmProblemDescription").send_keys("Test organisation problem " + self.current_date_time)
        sleep(self.test.sleep_time)
        Select(driver.find_element_by_id("frmProblemType")).select_by_visible_text("Logistics")
        sleep(self.test.sleep_time)
        Select(driver.find_element_by_id("frmProblemSubType")).select_by_visible_text("Legal Failure")
        sleep(self.test.sleep_time)
        driver.find_element_by_id("frmNoofPeopleAffected").clear()
        driver.find_element_by_id("frmNoofPeopleAffected").send_keys("10")
        sleep(self.test.sleep_time)
        Select(driver.find_element_by_id("frmProblemScope")).select_by_visible_text("One site")
        sleep(self.test.sleep_time)
        Select(driver.find_element_by_id("frmProblemStatus")).select_by_visible_text("New")
        sleep(self.test.sleep_time)
        Select(driver.find_element_by_id("frmProblemPriority")).select_by_visible_text("Major")
        sleep(self.test.sleep_time)
        driver.find_element_by_id("btn-problem-create").click()

        # view problem
        sleep(self.test.sleep_time)
        driver.find_element_by_link_text("Problem Overview").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_link_text("Problem History").click()

        sleep(self.test.sleep_time)
        # edit the problem
        driver.find_element_by_link_text("Edit Problem").click()
        sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "btn-problem-edit")))
        Select(driver.find_element_by_id("frmProblemStatus")).select_by_visible_text("Under investigation")
        sleep(self.test.sleep_time)
        driver.find_element_by_id("btn-problem-edit").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_id("frmProblemDescription").clear()
        driver.find_element_by_id("frmProblemDescription").send_keys("Test organisation problem. Further details added.")
        sleep(self.test.sleep_time)
        Select(driver.find_element_by_id("frmProblemAssignee")).select_by_visible_text("Graham Johnson-SU")
        driver.find_element_by_id("btn-problem-edit").click()
        sleep(self.test.sleep_time)
        # view the problem again
        driver.find_element_by_link_text("Problem Overview").click()

        sleep(self.test.sleep_time)
        # after editing problem check other tabs
        driver.find_element_by_link_text("Problem Overview").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_link_text("Problem History").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_link_text("Edit Problem").click()
        sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "btn-problem-edit")))
        Select(driver.find_element_by_id("frmProblemStatus")).select_by_visible_text("Resolved")
        Select(driver.find_element_by_id("frmProblemAssignee")).select_by_visible_text("Graham Johnson-SU")
        driver.find_element_by_id("btn-problem-edit").click()
        sleep(self.test.sleep_time)
        # view the problem again
        driver.find_element_by_link_text("Problem Overview").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_id("menu-top-problems").click()
        sleep(self.test.sleep_time)
        driver.find_element_by_id("menu-drop-problems").click()
        sleep(self.test.sleep_time)
        # driver.find_element_by_css_selector("#lnk-problem-delete-130 > i.fa.fa-trash-o").click()
        # self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to delete[\s\S]$")
        driver.find_element_by_css_selector("#lnkAdminMenu > b.caret").click()
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
