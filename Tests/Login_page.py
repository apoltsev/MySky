import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class LoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    #Check handling of correct user
    def test_success_login(self):
        driver = self.driver
        driver.get("https://client.mysky.com/login")
        self.assertIn("MySky", driver.title)
        elem_login = driver.find_element_by_name("login")
        elem_login.send_keys("correct_login")
        elem_psw = driver.find_element_by_name("password")
        elem_psw.send_keys("correct_password")
        elem_psw.send_keys(Keys.TAB)
        elem_psw.send_keys(Keys.RETURN)
        #assert 'Login failed' in driver.page_source - Test case is needed to update. Correct credentials are needed.

    #Check handling of non-existing user
    def test_non_existent_login(self):
        driver = self.driver
        driver.get("https://client.mysky.com/login")
        self.assertIn("MySky", driver.title)
        elem_login = driver.find_element_by_name("login")
        elem_login.send_keys("login")
        elem_psw = driver.find_element_by_name("password")
        elem_psw.send_keys("password")
        elem_psw.send_keys(Keys.TAB)
        elem_psw.send_keys(Keys.RETURN)
        assert 'Login failed' not in driver.page_source

    #Check handling with empty fields
    def test_empty_login(self):
        driver = self.driver
        driver.get("https://client.mysky.com/login")
        self.assertIn("MySky", driver.title)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div/button').click()
        WebDriverWait(driver, 3).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="app"]/div/div/form'), 'Login failed'))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()