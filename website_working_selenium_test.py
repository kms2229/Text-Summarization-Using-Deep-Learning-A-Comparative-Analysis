import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ChromeSearch(unittest.TestCase):
    def test_website_working(self):
        driver = webdriver.Chrome(executable_path=' ')
        driver.get(" ")
        self.assertIn(" ", driver.title)
        
    
if __name__ == "__main__":
    unittest.main()