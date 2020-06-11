# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# driver.execute_script("window.scrollBy(0,2800)", "")
#
# #rows = driver.find_element_by_xpath("//table[@name='BookTable']/tbody/tr").text
# rows =driver.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr")
#
# cols = driver.find_element_by_xpath("//table[@name='BookTable']/tbody/tr[1]/th").text
# print(rows)
# print(cols)

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()  # maximize window
driver.execute_script("window.scrollBy(0,1800)","")  # scroll down the page, optional , not mandatory

# 1) Count number of rows & columns
NoOfRows=len(driver.find_elements_by_xpath("//table[@name='BookTable']/tbody/tr")) # number of rows
NoOfColumns=len(driver.find_elements_by_xpath("//table[@name='BookTable']/tbody/tr[1]/th")) # number of columns

print(NoOfRows) #7
print(NoOfColumns)  #4
