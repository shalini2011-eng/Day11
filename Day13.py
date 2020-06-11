from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#driver = webdriver.Chrome()
#driver = webdriver.Ie()
driver = webdriver.Firefox()
time.sleep(5)

driver.get("http://demo.automationtesting.in/Register.html")
#driver.maximize_window()

#dropdown =  Select(driver.find_element_by_xpath("//div[@id='msdd']"))
dropdown = Select(driver.find_element_by_id("Skills"))

total_Count = len(dropdown.options)
print("Length of dropdown is:", total_Count)

#dropdown.select_by_visible_text("Analytics")
#dropdown.select_by_index(3)
dropdown.select_by_value("5")

all_options = dropdown.options
for option in all_options:
    print(option.text)


