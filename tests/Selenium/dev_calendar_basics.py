import unittest, time, re
from time import sleep

# selenium imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# tests imports
from tests.Selenium.functions.properties_test import TestProperties
from tests.Selenium.functions.login import login

class CalendarBasics(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
    
    def test_dev_calendar_basics(self):
        driver = self.driver

        driver.get(self.base_url + "/")

        login(self, driver)

        driver.maximize_window()
        sleep(self.test.sleep_time)

        element = WebDriverWait(driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, "menu-top-time")))

        # create task
        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "menu-top-project"))
        )
        driver.find_element_by_id("menu-top-project").click()
        element = WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "menu-drop-projects"))
        )
        driver.find_element_by_id("menu-drop-projects").click()

        # go to view test project
        element = WebDriverWait(driver, self.wait_time).until(
            expected_conditions.element_to_be_clickable((By.ID, "tbProjectIndex_info")))
        link = "lnkView" + self.test.test_project[0:8]
        driver.find_element_by_id(link).click()

        sleep(self.test.sleep_time)

        # Add tasklist to project (in case there isn't one)
        driver.find_element_by_id("button-tkl").click()

        element = WebDriverWait(driver, self.wait_time).until(
            expected_conditions.element_to_be_clickable((By.ID, "btn-tasklist-create")))


        driver.find_element_by_id("frmTaskListName").clear()
        driver.find_element_by_id("frmTaskListName").send_keys("Test tasklist " + self.test.test_time)
        driver.find_element_by_id("frmTaskListDescription").clear()
        driver.find_element_by_id("frmTaskListDescription").send_keys("Test tasklist" + self.test.test_time)
        driver.find_element_by_id("btn-tasklist-create")

        sleep(self.test.sleep_time)

        driver.find_element_by_class_name("task-add").click()
        element = WebDriverWait(driver, self.wait_time).until(
            EC.visibility_of_element_located((By.ID, "btn-task-add"))
        )

        # add task
        driver.find_element_by_id("frmTaskName").clear()
        driver.find_element_by_id("frmTaskName").send_keys("Test tasklist " + self.test.test_time)
        driver.find_element_by_id("frmTaskDescription").clear()
        driver.find_element_by_id("frmTaskDescription").send_keys("Test tasklist  " + self.test.test_time)
        Select(driver.find_element_by_id("frmTaskType")).select_by_visible_text("Execution")
        Select(driver.find_element_by_id("frmTaskPriority")).select_by_visible_text("Medium")
        Select(driver.find_element_by_id("frmTaskStatus")).select_by_visible_text("New")
        Select(driver.find_element_by_id("frmTaskAssignee")).select_by_index(2)
        driver.find_element_by_class_name("date-task-start").click()
        driver.find_element_by_link_text("28").click()
        driver.find_element_by_id("frmEstimatedTime").clear()
        driver.find_element_by_id("frmEstimatedTime").send_keys("2")
        driver.find_element_by_id("frmPercentageComplete").clear()
        driver.find_element_by_id("frmPercentageComplete").send_keys("0")

        driver.find_element_by_id("btn-task-add").click()

        sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(
            expected_conditions.element_to_be_clickable((By.ID, "menu-top-time")))

        # visit calendar
        driver.find_element_by_id("menu-top-time").click()
        sleep(self.test.sleep_time)
        element = WebDriverWait(driver, self.wait_time).until(
            EC.visibility_of_element_located((By.ID, "menu-drop-calendar"))
        )
        sleep(self.test.sleep_time)
        driver.find_element_by_id("menu-drop-calendar").click()
        sleep(self.test.sleep_time)

        self.test.find_item_in_table("tbCalendar", "td", "Test tasklist " + self.test.test_time)


        # log out
        driver.find_element_by_css_selector("#lnkAdminMenu > b.caret").click()
        element = WebDriverWait(driver, self.wait_time).until(
            EC.visibility_of_element_located((By.ID, "logout"))
        )
        sleep(self.test.sleep_time)
        driver.find_element_by_id("logout").click()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
