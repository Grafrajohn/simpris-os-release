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

class ProjectBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.wait_time = self.test.wait_time
    
    def test_project_basics(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        login(self, driver)

        driver.maximize_window()

        # Create project
        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "menu-top-project"))
        )
        driver.find_element_by_id("menu-top-project").click()
        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "menu-drop-project-create"))
        )
        sleep(self.test.sleep_time)
        driver.find_element_by_id("menu-drop-project-create").click()
        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "frmProjectAdd"))
        )
        Select(driver.find_element_by_id("frmProjectOrganisation")).select_by_visible_text("Northern Media Services")
        driver.find_element_by_id("frmProjectName").clear()
        driver.find_element_by_id("frmProjectName").send_keys("Test project")
        driver.execute_script("CKEDITOR.instances['frmProjectDescription'].setData('<p>Test project description</p>');")
        driver.execute_script("CKEDITOR.instances['frmProjectDeliverables'].setData('<p>Test project deliverables</p>');")
        driver.find_element_by_id("frmProjectBudget").clear()
        driver.find_element_by_id("frmProjectBudget").send_keys("150000")
        Select(driver.find_element_by_id("frmProjectImportance")).select_by_visible_text("Medium")
        driver.find_element_by_id("btn-project-create").click()

        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "menu-project-edit"))
        )

        # Edit project
        driver.find_element_by_id("menu-project-edit").click()
        #driver.find_element_by_id("cke_frmProjectDescription").clear()
        driver.execute_script("CKEDITOR.instances['frmProjectDescription'].setData('<p>Test project description enhanced</p>');")
        #driver.find_element_by_id("cke_frmProjectDescription").send_keys("Test project description enhanced.")
        driver.find_element_by_id("btn-project-edit").click()

        # Navigate around
        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "footer-copyright"))
        )
        driver.find_element_by_link_text("Project Users").click()
        driver.find_element_by_link_text("Project History").click()
        driver.find_element_by_link_text("Project Overview").click()

        # Create tasklist
        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "footer-copyright"))
        )
        driver.find_element_by_id("button-tkl").click()
        driver.find_element_by_id("frmTaskListName").clear()
        driver.find_element_by_id("frmTaskListName").send_keys("Test tasklist")
        driver.find_element_by_id("frmTaskListDescription").clear()
        driver.find_element_by_id("frmTaskListDescription").send_keys("Test tasklist description")
        driver.find_element_by_id("btn-tasklist-create").click()

        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "projectPanel"))
        )

        sleep(self.test.sleep_time)

        # Add task
        driver.find_element_by_class_name("task-add").click()
        #driver.find_element_by_id("frmTaskDescription").clear()
        driver.execute_script("CKEDITOR.instances['frmTaskDescription'].setData('<p>Test task description</p>');")
        #driver.find_element_by_id("frmTaskDescription").send_keys("Test task")
        Select(driver.find_element_by_id("frmTaskType")).select_by_visible_text("Execution")
        Select(driver.find_element_by_id("frmTaskPriority")).select_by_visible_text("Medium")
        Select(driver.find_element_by_id("frmTaskStatus")).select_by_visible_text("New")
        Select(driver.find_element_by_id("frmTaskAssignee")).select_by_visible_text("Graham Johnson-SU")
        driver.find_element_by_class_name("hasDatepicker").click()
        driver.find_element_by_link_text("28").click()
        driver.find_element_by_id("frmEstimatedTime").clear()
        driver.find_element_by_id("frmEstimatedTime").send_keys("2")
        driver.find_element_by_id("frmPercentageComplete").clear()
        driver.find_element_by_id("frmPercentageComplete").send_keys("0")
        driver.find_element_by_id("btn-task-add").click()

        sleep(self.test.sleep_time)

        # Edit tasklist
        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, "tasklist-edit"))
        )
        driver.find_element_by_class_name("tasklist-edit").click()
        driver.find_element_by_id("frmTaskListDescription").clear()
        driver.find_element_by_id("frmTaskListDescription").send_keys("Test tasklist description enhanced")
        driver.find_element_by_id("btn-tasklist-edit").click()

        #driver.find_element_by_link_text("Edit").click()
        #driver.find_element_by_link_text("Edit").click()
        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "lnkAdminMenu"))
        )
        driver.find_element_by_id("lnkAdminMenu").click()
        driver.find_element_by_id("logout").click()
        # driver.find_element_by_id("username").clear()
        # driver.find_element_by_id("username").send_keys("user-name")
        # driver.find_element_by_id("password").clear()
        # driver.find_element_by_id("password").send_keys("password")
    
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
