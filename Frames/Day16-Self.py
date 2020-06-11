from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()

#driver.execute_script("window.scrollBy(0,2000)","")


# flag=driver.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody")
# driver.execute_script("arguments[0].scrollIntoView();",flag)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)

#driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")

# rows=len(driver.find_elements_by_xpath("//table[@name='BookTable']/tbody/tr"))
# cols=len(driver.find_elements_by_xpath("//table[@name='BookTable']/tbody/tr[1]/th"))
# print(rows)
# print(cols)