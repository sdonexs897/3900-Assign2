import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "instructor"
        pwd = "maverick2"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        driver.find_element_by_css_selector('#content-main')
        time.sleep(5)

        if driver is not None:
            print('Found CSS selector element')



