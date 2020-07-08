from selenium import webdriver

import time
import pytest

class Test_homepage():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/development/Selenium/Webdrivers/chromedriver.exe")
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        driver.close()
        driver.quit()

    def test_login(self,test_setup):
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        title = driver.title
        assert title == "OrangeHRM"

    def test_admin(self,test_setup):
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_xpath("//b[contains(text(),'Admin')]").click()
        time.sleep(5)

    def test_admin2(self,test_setup):
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_xpath("//b[contains(text(),'Admin')]").click()
        time.sleep(5)
