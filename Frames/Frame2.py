from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Frames.html")
driver.maximize_window()
# driver.switch_to.frame("SingleFrame")
# driver.find_element_by_xpath("//input[@type='text']").send_keys("Shalini")

#driver.find_element_by_xpath("//a[@class='analystic' and @xpath=2]").click()
driver.find_element_by_xpath("//a[@class='analystic' and @href='#Multiple']").click()
OuterFrame=driver.find_element_by_xpath("//iframe[@src = 'MultipleFrames.html']")
driver.switch_to.frame(OuterFrame)
InnerFrame = driver.find_element_by_xpath("//iframe[@src = 'SingleFrame.html']")
driver.switch_to.frame(InnerFrame)
driver.find_element_by_xpath("//input[@type='text']").send_keys("Shalini")