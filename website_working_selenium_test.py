import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ChromeSearch(unittest.TestCase):
    def test_website_working(self):
        driver = webdriver.Chrome(executable_path='C:/Users/shahk/chromedriver_win32/chromedriver.exe')
        driver.get("https://bu-marketplace.herokuapp.com/log_in")
        self.assertIn("BU MarketPlace", driver.title)
        
    
if __name__ == "__main__":
    unittest.main()