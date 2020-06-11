# from selenium import webdriver
# from selenium.webdriver import ActionChains
# import time
#
# driver = webdriver.Chrome()
#
# driver.get("http://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# CopyText=driver.find_element_by_xpath("//button[contains(text(),'Copy Text')]")
#
# action = ActionChains(driver)

#action.double_click(CopyText).perform()


# from selenium import webdriver
# from selenium.webdriver import ActionChains
# import time
#
# driver = webdriver.Chrome()
#
# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# driver.maximize_window()
#
# source_element = driver.find_element_by_xpath("//div[text()='Oslo' and @id = 'box1']")
# target_element = driver.find_element_by_xpath("//div[@id='box106' and text() ='Italy']")
#
# action = ActionChains(driver)
# action.drag_and_drop(source_element,target_element).perform()
#
# src_Stockholm = driver.find_element_by_xpath("//div[@id='box2' and text()= 'Stockholm']")
# trg_us = driver.find_element_by_xpath("//div[@id='box103' and text()='United States']")
# action.drag_and_drop(src_Stockholm,trg_us).perform()


from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button =driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")
action = ActionChains(driver)
action.context_click(button).perform()
time.sleep(5)
driver.find_element_by_xpath("//span[text()='Copy']").click()

alert =driver.switch_to.alert
print(alert.text)
alert.accept()

time.sleep(5)
driver.close()