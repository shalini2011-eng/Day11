# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# driver = webdriver.Chrome()
#
# driver.get("http://www.practiceselenium.com/practice-form.html")
# driver.maximize_window()
#
# list1 = Select(driver.find_element_by_css_selector("select[id ='selenium_commands']"))
# total_list_count = len(list1.options)
# print("total elements of list are:", total_list_count)
#
# list1.select_by_visible_text("Browser Commands")
# list1.select_by_visible_text("Switch Commands")
#
# all_options = list1.options
# for opt in all_options:
#     print(opt.text)


#Navigational commands

from selenium import webdriver
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.amazon.in/")
print(driver.title)

driver.get("https://www.snapdeal.com/")
print(driver.title)

driver.back()
print(driver.title) #amazon

driver.forward()
print(driver.title) #Snapdeal

driver.refresh()
driver.close()
