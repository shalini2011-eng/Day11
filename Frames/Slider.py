from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver =webdriver.Chrome()
driver.get("https://jqueryui.com/slider/")
driver.maximize_window()

driver.switch_to.frame(0)
time.sleep(5)
action = ActionChains(driver)

slider=driver.find_element_by_xpath("//div[@id='slider']")
print(slider.location)

action.move_to_element(slider).drag_and_drop_by_offset(slider,500,0).perform()
print(slider.location)
