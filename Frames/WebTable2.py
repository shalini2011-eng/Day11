from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()  # maximize window
#driver.execute_script("window.scrollBy(0,1800)","")  # scroll down the page, optional , not mandatory

element = driver.find_element_by_xpath("//div[@id='HTML1']")
driver.execute_script("arguments[0].scrollIntoView();", element)

# 1) Count number of rows & columns
NoOfRows=len(driver.find_elements_by_xpath("//table[@name='BookTable']/tbody/tr")) # number of rows
NoOfColumns=len(driver.find_elements_by_xpath("//table[@name='BookTable']/tbody/tr[1]/th")) # number of columns

# print(NoOfRows) #7
# print(NoOfColumns)  #4

#2) reading specific row & Column
#data=driver.find_element_by_xpath("//table[@name='BookTable']/tbody/tr[5]/td[1]").text
#print(data)

#3) Read all the rows & Columns data
print("Printing all column values: ")
for r in range(2,NoOfRows+1):
    for c in range(1,NoOfColumns+1):
        value = driver.find_element_by_xpath("//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='            ')
    print()

# 4) Read data based on condition(List books name whose author is Mukesh)
# for r in range(2,NoOfRows+1):
#     authorName = driver.find_element_by_xpath("//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
#     if authorName=="Mukesh":
#         bookName=driver.find_element_by_xpath("//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
#         print(bookName,"       ",authorName)
