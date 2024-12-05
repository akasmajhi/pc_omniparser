#This code runs the unittest discovery process to find and execute all test cases in the 'tests' directory that match the pattern 'custom_pattern*.py'. This is a common way to run a test suite in a Python project.
#python -m unittest discover -s tests -p "custom_pattern*.py"

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config.config import CHROME_DRIVER_PATH, URL

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.driver.get(URL)

    def test_valid_login_admin(self):
        driver = self.driver
        # Locate fields
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        role_dropdown = driver.find_element(By.NAME, "role")
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")

        # Input valid data
        username_field.send_keys("pravash")
        password_field.send_keys("password")
        role_dropdown.send_keys("Admin")  # Select "Admin" from dropdown
        login_button.click()

        # Validation: Check for a successful login
        # Adjust the expected behavior depending on the success page or message
        success_message = driver.find_element(By.XPATH, "//h1[text()='Welcome Admin']")
        self.assertIsNotNone(success_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
