import time
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestProperties:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"
        self.live_base_url = "https://www.simpris.com"
        self.wait_time = 10
        self.test_time = time.strftime('%Y-%m-%d-%H-%M-%S')
        self.sleep_time = 1

        self.username = 'user-name'
        self.password = 'password'

        self.test_organisation = "Northern Media Services"
        self.test_project = "NMS Test"

        self.browser = "CH"
        self.OS = "MAC" #WIN/MAC/LIN
        self.driver = None
        if self.browser == "ED":
            driver_path = 'C:\\source\\simpris\\tests\\drivers\\MicrosoftWebDriver.exe'
            self.driver = webdriver.Edge(driver_path)
        elif self.browser == "CH":
            if self.OS == "MAC":
                driver_path = '/Applications/chromedriver'
                    #'/Source/Simpris/tests/Selenium/drivers/chromedriver'
                self.driver = webdriver.Chrome(driver_path)
            else:
                driver_path = 'C:\\source\\simpris\\tests\\drivers\\chromedriver.exe'
                self.driver = webdriver.Chrome(driver_path)
        elif self.browser == "SA":
            if self.OS == "MAC":
                driver_path = '/usr/bin/safaridriver'
                self.driver = webdriver.Safari(driver_path)
            else:
                driver_path = 'C:\\source\\simpris\\tests\\drivers\\chromedriver.exe'
                self.driver = webdriver.Safari(driver_path)
        elif self.browser == "FF":
            if self.OS == "MAC":
                driver_path = '/Applications/geckodriver'
                caps = DesiredCapabilities.FIREFOX
                caps["marionette"] = True
                caps["binary"] = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"
                self.driver = webdriver.Firefox(capabilities=caps,executable_path=driver_path)
            else:
                driver_path = 'C:\\source\\simpris\\tests\\drivers\\geckodriver.exe'
                caps = DesiredCapabilities.FIREFOX
                caps["marionette"] = True
                self.driver = webdriver.Firefox(capabilities=caps,executable_path=driver_path)
        elif self.browser == "IE":
            driver_path = 'C:\\source\\simpris\\tests\\drivers\\iedriver.exe'
            self.driver = webdriver.Ie(driver_path)
        else:
            raise ValueError('You have not configured a webdriver!')
        #self.driver.implicitly_wait(self.wait_time)

    def find_item_and_link_in_table(self, table_name, item_type, search_text, link_text):
        table = self.driver.find_element_by_id(table_name)
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            for link in row.find_elements_by_tag_name("a"):
                if link.text == link_text:
                    link_cell = link
            for cell in row.find_elements_by_tag_name("td"):
                if cell.text == search_text:
                    return link_cell

    # def find_item_in_table_row(self, row, item_type, search_text):
    #     item_found = False
    #     for cell in row:
    #         lnk = cell.find_elements_by_tagname("a")
    #         if lnk is not None:
    #             return lnk

    def find_item_in_table(self, table_name, item_type, search_text):
        table = self.driver.find_element_by_id(table_name)
        item_found = False
        for cell in table.find_elements_by_tag_name(item_type):
            if cell.text in search_text:
                item_found = cell
        return item_found

    def find_item_in_div(self, div_name, search_text, search_tags):
        div = self.driver.find_element_by_id(div_name)
        item_found = False
        for item in div.find_elements_by_tag_name(search_tags):
            if item.text in search_text:
                item_found = item
        return item_found

    def find_item_in_list(self, list_name, search_text, search_tags):
        list = self.driver.find_element_by_id(list_name)
        item_found = False
        for item in list.find_elements_by_tag_name(search_tags):
            if item.text in search_text:
                item_found = item
        return item_found

    def refresh_page(self):
        self.driver.refresh()

    def maximise_window(self):
        self.driver.maximize_window()

    def wait_for_element_clickable(self, element_id):
        element = WebDriverWait(self.driver, self.wait_time).until(expected_conditions.element_to_be_clickable((By.ID, element_id)))

    def wait_for_element_visible(self, element_id):
        element = WebDriverWait(self.driver, self.wait_time).until(expected_conditions.visibility_of_element_located((By.ID, element_id)))

    def click_and_hold(self, element):
        ActionChains(self.driver).click_and_hold(element).perform()

    def drag_and_drop_elements(self, source_element_in, dest_element_in):
        #source_element = self.driver.find_element_by_class_name(source_element_in)
        #dest_element = self.driver.find_element_by_id(dest_element_in)
        ActionChains(self.driver).drag_and_drop(source_element_in, dest_element_in).perform()

    def drag_and_drop_ids(self, source_element_in, dest_element_in):
        source_element = self.driver.find_element_by_class_name(source_element_in)
        dest_element = self.driver.find_element_by_id(dest_element_in)
        ActionChains(self.driver).drag_and_drop(source_element_in, dest_element_in).perform()

    # commonly used functions
    # create task

