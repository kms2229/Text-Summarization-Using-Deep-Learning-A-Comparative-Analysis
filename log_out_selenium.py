import unittest
from random import randint
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class ChromeSearch(unittest.TestCase):
    def test_log_out_working(self):
        driver = webdriver.Chrome(executable_path=' ')
        driver.get(" ")
        email = " "
        passwr = " "
# find username/email field and send the username itself to the input field
        driver.find_element_by("id","email").send_keys(email)
# find password input field and insert password as well
        driver.find_element("id","password").send_keys(passwr)
    # click login button
        driver.find_element("name","login").click()
        sleep(2)    
    # click logout button
        driver.find_element("id","log_out").click()
        sleep(2)    
        try:
            driver.find_element_by_xpath(" ")
            s="done"
        except:
            s="Incorrect."        

        self.assertIn(s,"done")

# close the driver
        driver.close()
    
if __name__ == "__main__":
    unittest.main()
