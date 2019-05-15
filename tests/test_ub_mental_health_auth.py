import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class UBMentalHealthAuth(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_title(self):
        driver = self.driver
        driver.get("https://ubmentalhealth.herokuapp.com/login?next=%2F")
        self.assertIn("Sign In - Mental Health App", driver.title)

    def test_register(self):
        driver = self.driver
        driver.get("https://ubmentalhealth.herokuapp.com/login?next=%2F")
        driver.implicitly_wait(5)
        username = driver.find_element_by_name("username")
        driver.implicitly_wait(1)
        username.send_keys("admin_testing")
        driver.implicitly_wait(1)
        password = driver.find_element_by_name("password")
        driver.implicitly_wait(1)
        password.send_keys("changeme")
        driver.implicitly_wait(1)
        submit = driver.find_element_by_name("submit")
        driver.implicitly_wait(1)
        submit.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        # wait = WebDriverWait(driver, 10)
        assert driver.find_element_by_id("myCarousel").is_displayed()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
