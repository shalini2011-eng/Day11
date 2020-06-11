from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)

driver.find_element_by_xpath("//div[@id='Tabbed']//button[@class='btn btn-info'][contains(text(),'click')]").click()

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)



