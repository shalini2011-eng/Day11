import pytest
import time

class TestParallelTesting:
    def test_loginFromChrome(self,setup):
        #self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.get_screenshot_as_file("D:\Download_Python_File\Login_Page.jpeg")
        assert self.driver.title == 'OrangeHRM'


        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()

        self.actual_title =self.driver.title
        assert self.actual_title == 'OrangeHRM'
        self.driver.get_screenshot_as_file("D:\Download_Python_File\FirstPage.jpeg")
        self.driver.close()

    # def test_loginFromIe(self):
    #     self.driver = webdriver.Ie()
    #     self.driver.maximize_window()
    #     #self.driver.implicitly_wait(5)
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/")
    #     assert self.driver.title == 'OrangeHRM'
    #
    #     self.driver.find_element_by_id("txtUsername").send_keys("Admin")
    #     self.driver.find_element_by_css_selector("input#txtPassword").send_keys("admin123")
    #     self.driver.find_element_by_css_selector("input#btnLogin").click()
    #
    #     self.actual_title = self.driver.title
    #     assert self.actual_title == 'OrangeHRM'
    #     self.driver.close()

    # def test_loginFromFirefox(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(5)
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/")
    #     assert self.driver.title == 'OrangeHRM'
    #
    #     self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
    #     self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
    #     self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()
    #
    #     self.actual_title = self.driver.title
    #     assert self.actual_title == 'OrangeHRM'
    #     self.driver.close()

# obj = TestParallelTesting()
# obj.test_loginFromIe()