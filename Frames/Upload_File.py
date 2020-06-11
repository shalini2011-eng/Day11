from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("admin")
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//input[@id='btnLogin']").click()

driver.find_element_by_xpath("//b[contains(text(),'PIM')]").click()
driver.find_element_by_xpath("//input[@id='btnAdd']").click()

driver.find_element_by_xpath("//input[@id='photofile']").send_keys("D:\Download_Python_File\odyPartNurseryEdited.pdf")
