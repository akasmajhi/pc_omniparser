#This code runs the unittest discovery process to find and execute all test cases in the 'tests' directory that match the pattern 'custom_pattern*.py'. This is a common way to run a test suite in a Python project.
#python -m unittest discover -s tests -p "custom_pattern*.py"
#python -m unittest discover tests
import unittest
import time  # Import time for sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from config.config import CHROME_DRIVER_PATH, URL

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ##Original below
        # self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        #self.driver.get(URL)
        self.driver.get("http://127.0.0.1:5500/site/autogen-demo/index.html" )
        time.sleep(2)  # Pause for 2 seconds after the browser launches

    def test_valid_login_admin(self):
        driver = self.driver
        # Locate fields
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        role_dropdown = driver.find_element(By.NAME, "role")
        #login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
        
        #Adding the "Login" button is an <input> element with the type="submit" attribute. 
        login_button = driver.find_element(By.XPATH, "//input[@type='submit']")

        # Input valid data
        username_field.send_keys("pravash")
        time.sleep(1)
        password_field.send_keys("password")
        time.sleep(1)
        role_dropdown.send_keys("Admin")  # Select "Admin" from dropdown
        time.sleep(1)
        login_button.click()
        time.sleep(2)

        # Validation: Check for a successful login
        
                #  Verify redirection to the role-specific page
        expected_url = "http://127.0.0.1:5500/site/admin.html"  # Replace with actual Admin URL
        if driver.current_url == expected_url:
            print("Successfully redirected to the Admin page.")
        else:
            print("Redirection failed. Current URL:", driver.current_url)

    # Step 6: Verify the personalized message
        lbl_username = driver.find_element(By.ID, "lbl_username").text
        expected_message = "Hello, akas! This is the landing page for the Admin!"
        if lbl_username == expected_message:
            print("Role-based message verified successfully.")
        else:
         print("Role-based message mismatch. Actual message:", lbl_username)


    def tearDown(self):
        self.driver.quit()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
