from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

Frame = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
driver.switch_to.frame(Frame)

#driver.find_element_by_xpath("//input[@id='datepicker']").send_keys("10/15/2020")

day = '30'
mon = 'November'
yr = '2020'

driver.find_element_by_xpath("//input[@id='datepicker']").click()
while True:
    year = driver.find_element_by_xpath("//span[@class='ui-datepicker-year']").text
    #print(year)
    if year == yr:
        print(year)
        break
    else:
        driver.find_element_by_xpath("//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

while True:
    month = driver.find_element_by_xpath("//span[@class='ui-datepicker-month']").text
    #print(month)
    if month == mon:
        print(month)
        break
    else:
        driver.find_element_by_xpath("//span[@class='ui-icon ui-icon-circle-triangle-e']").click()


dates = driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
#print(dates)
for date in dates:
   if date.text == day:
       date.click()
       break



