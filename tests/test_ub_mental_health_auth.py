import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class UBMentalHealthAuth(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_title(self):
        driver = self.driver
        driver.get("http://www.ubmentalhealth.heroku.org")
        self.assertIn("Sign In - Mental Health App", driver.title)

    def test_register(self):
        driver = self.driver
        driver.get("http://www.ubmentalhealth.heroku.org")
        self.assertIn("Sign In - Mental Health App", driver.title)
        username = driver.find_element_by_name("username")
        username.send_keys("1_test_user_to_rule_them_all")
        password = driver.find_element_by_name("password")
        password.send_keys("g5E483&^s34fEl%W")
        submit = driver.find_element_by_name("submit")
        submit.send_keys(Keys.RETURN)
        self.assertIn("Home - Mental Health App", driver.title)
        assert "Hi,  1_test_user_to_rule_them_all" in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
