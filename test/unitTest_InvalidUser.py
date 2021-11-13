import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "sdot27"
        pwd = "maverick2"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(3)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)

        if driver is not None:
            print('Invalid Credentials')


if __name__ == '__main__':
    unittest.main()
