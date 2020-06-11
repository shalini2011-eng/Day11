# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
#
# driver.get("http://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# element = driver.find_element_by_xpath("//div[@id='HTML1']")
# driver.execute_script("arguments[0].scrollIntoView();", element)
# time.sleep(2)
#
# rows = len(driver.find_elements_by_xpath("//table[@name = 'BookTable']/tbody/tr"))
# cols = len(driver.find_elements_by_xpath("//table[@name = 'BookTable']/tbody/tr[2]/td"))
# #
# # print(rows)
# # print(cols)
#
# #rows= driver.find_element_by_xpath("//table[@name = 'BookTable']/tbody/tr[1]").text
# #cols = driver.find_element_by_xpath("//table[@name = 'BookTable']/tbody/tr[1]/th").text
#
# #print(rows)
# #print(cols)
#
# for r in range(2, rows+1):
#     for c in range(1, cols+1):
#         val = driver.find_element_by_xpath("//table[@name = 'BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(val, end='   ')
#     pri
