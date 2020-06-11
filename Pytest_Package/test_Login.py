# import pytest
#
#
# class TestLogin:
#     @pytest.mark.run(order=5)
#     @pytest.mark.sanity
#     @pytest.mark.regression
#     def test_loginByEmail(self,setup):
#         print("Login by email")
#         assert 1 == 1
#
#     @pytest.mark.run(order=4)
#     @pytest.mark.sanity
#     @pytest.mark.regression
#     def test_loginByFacebook(self,setup):
#         print("login by facebook")
#         assert 1 == 1
#
#     @pytest.mark.run(order=2)
#     @pytest.mark.regression
#     def test_loginByTwitter(self,setup):
#         print("login by twitter")
#         assert 1 == 1
#
#     @pytest.mark.run(order=3)
#     @pytest.mark.sanity
#     @pytest.mark.regression
#     def test_loginByInsta(self,setup):
#         print("login By insta")
#         assert True == True
#
#     @pytest.mark.run(order=1)
#     @pytest.mark.regression
#     def test_loginByLinkedin(self, setup):
#         print("login by linkedin")
#         assert 1 == 1

from selenium import webdriver

class Testing:
    def func1(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()

Obj1 = Testing()
Obj1.func1()



