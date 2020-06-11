from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("http://testautomationpractice.blogspot.com/")
#
# driver.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()
# driver.switch_to.alert.accept()
#
# Label =driver.find_element_by_xpath("//p[text()= 'You pressed OK!']").text
# print(Label)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.switch_to.frame("packageListFrame")
driver.find_element_by_xpath("//a[text()='org.openqa.selenium']").click()
driver.switch_to.default_content()
# AddCookie=driver.find_element_by_xpath("//a[text()='AddCookie']")
driver.switch_to.frame("packageFrame")
driver.find_element_by_xpath("//span[text()='OutputType']").click()
driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
# driver.find_element_by_xpath("//li[@class='navBarCell1Rev'][text()='Index']")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[6]").click()
#driver.find_element_by_xpath("//div[@class='topNav']//li[@class='navBarCell1Rev'][contains(text(),'Index')]").click()
