from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

# driver.find_element_by_id("txtUsername").send_keys("Admin")
# driver.find_element_by_id("txtPassword").send_keys("admin123")

driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")


driver.find_element_by_name("Submit").click()
act_title = driver.title
Exp_title = "OrangeHRM"
if act_title == Exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")


print("Page title is :",  driver.title)
print("Current URL is:",  driver.current_url)
print("Page spurce is :", driver.page_source)





