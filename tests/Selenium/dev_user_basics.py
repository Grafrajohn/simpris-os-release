# from Python
import unittest, time, re
from time import sleep

# from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from Simpris
from tests.Selenium.functions.properties_test import TestProperties
from tests.Selenium.functions.login import login
from tests.Selenium.functions.logout import logout

class PythonUserTest(unittest.TestCase, TestProperties):
    def setUp(self):
        self.test = TestProperties()
        self.driver = self.test.driver
        self.driver.implicitly_wait(self.test.wait_time)
        self.base_url = self.test.base_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.current_date_time = self.test.test_time
        self.wait_time = self.test.wait_time
        self.test.sleep_time
    
    def test_python_user(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        login(self, driver)

        driver.maximize_window()

        driver.find_element_by_id("menu-top-people").click()
        driver.find_element_by_id("menu-drop-user-create").click()
        #driver.find_element_by_link_text("People & Clients").click()

        WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "btn-user-create"))
        )

        #driver.find_element_by_link_text("Add user").click()
        driver.find_element_by_id("frmUsername").clear()
        driver.find_element_by_id("frmUsername").send_keys("Jimmy_" + self.current_date_time)
        driver.find_element_by_id("frmFirstName").clear()
        driver.find_element_by_id("frmFirstName").send_keys("Jimmy")
        driver.find_element_by_id("frmLastName").clear()
        driver.find_element_by_id("frmLastName").send_keys("Test")
        driver.find_element_by_id("frmEmail").clear()
        driver.find_element_by_id("frmEmail").send_keys(self.current_date_time + "@email.com")
        driver.find_element_by_id("frmPhone").clear()
        driver.find_element_by_id("frmPhone").send_keys("01234 12345678")
        Select(driver.find_element_by_id("frmOrganisation")).select_by_visible_text("Test-Organisation")
        driver.find_element_by_id("frmPassword").clear()
        driver.find_element_by_id("frmPassword").send_keys("password")
        driver.find_element_by_id("frmPasswordConfirm").clear()
        driver.find_element_by_id("frmPasswordConfirm").send_keys("password")
        driver.find_element_by_id("btn-user-create").click()

        driver.find_element_by_link_text("User History").click()
        driver.find_element_by_link_text("Edit User").click()
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "frmUserEdit"))
        # )
        driver.find_element_by_id("frmLastName").clear()
        driver.find_element_by_id("frmLastName").send_keys("Test_" + self.current_date_time)
        driver.find_element_by_id("btn-user-edit").click()

        sleep(self.test.sleep_time)
        WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located((By.LINK_TEXT, "User Overview"))
        )

        driver.find_element_by_link_text("User Overview").click()

        WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located((By.LINK_TEXT, "User History"))
        )

        driver.find_element_by_link_text("User History").click()

        WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located((By.ID, "lnkAdminMenu"))
        )

        # logout
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
