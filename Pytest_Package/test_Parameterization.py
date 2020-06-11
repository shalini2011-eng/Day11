import pytest

from selenium import webdriver

class TestnopCommerce:
    @pytest.mark.parametrize(
        'user, password',
        [
            ('admin@yourstore.com','admin'),
            ('admin@yourstrore.com','adm'),
            ('admin@yourstro.com','admin'),
            ('admin@yourstroe.com','adin')
        ]
    )

    def test_login(self,user,password):
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.driver.get_screenshot_as_file("Login_Page.jpeg")

        self.driver.find_element_by_xpath("//input[@id='Email']").clear()
        self.driver.find_element_by_xpath("//input[@id='Email']").send_keys(user)
        self.driver.find_element_by_xpath("//input[@id='Password']").clear()
        self.driver.find_element_by_xpath("//input[@id='Password']").send_keys(password)
        self.driver.find_element_by_xpath("//input[@class='button-1 login-button']").click()
        self.actual_title = self.driver.title
        print(self.actual_title)
        self.driver.get_screenshot_as_file("1st_Page.jpeg")
        self.driver.close()
        assert self.actual_title == "Dashboard / nopCommerce administration"