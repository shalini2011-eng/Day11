from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()

# driver.find_element_by_xpath("//input[@placeholder='First Name']").clear()
# print(" Whether TextBox is displayed?  :", driver.find_element_by_xpath("//input[@placeholder='First Name']").is_displayed() )
# print("Whether Textbox is enabled? :", driver.find_element_by_xpath("//input[@placeholder='First Name']").is_enabled())
# driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Shalini")
#
# driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Teotia")

# driver.find_element_by_xpath("//textarea[@class='form-control ng-pristine ng-valid ng-touched']").send_keys("Test Area")
# print("Whether Text Area displayed:", driver.find_element_by_css_selector("//textarea[@class='form-control ng-pristine ng-valid ng-touched']").is_displayed())
# print ("Whether Text Area s enabled", driver.find_element_by_xpath("//textarea[@class='form-control ng-pristine ng-valid ng-touched']").is_enabled() )
# driver.find_element_by_xpath("//textarea[@class='form-control ng-pristine ng-valid ng-touched']").send_keys("Its text area")

#time.sleep(20)
# Radio buttton
# MaleRadioButton =driver.find_element_by_css_selector("input[value=Male]")
# print("Whether Male Radio button is displayed?", MaleRadioButton.is_displayed() )
# print("Whether Male Radio button is enabled?", MaleRadioButton.is_enabled())
# print("Whether Male radio button is selected?", MaleRadioButton.is_selected())
# MaleRadioButton.click()
# print("Male Radio button after click:", MaleRadioButton.is_selected())

#Female Radio button
#
FeMaleRadioButton =driver.find_element_by_css_selector("input[value=FeMale]")
print("Whether Male Radio button is displayed?", FeMaleRadioButton.is_displayed() )
print("Whether Male Radio button is enabled?", FeMaleRadioButton.is_enabled())
print("Whether Male radio button is selected?", FeMaleRadioButton.is_selected())
FeMaleRadioButton.click()
#
# print("FeMale Radio button after click:", FeMaleRadioButton.is_selected())

# driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[5]/div/label[2]/input").click()

# Chkbox_Cricket =driver.find_element_by_css_selector("input[value = Cricket]")
# print(Chkbox_Cricket.is_displayed())
# print(Chkbox_Cricket.is_enabled())
# time.sleep(5)
# print("Status for Cricket Checkbox is :", Chkbox_Cricket.is_selected())
# Chkbox_status  = Chkbox_Cricket.is_selected()
# if Chkbox_status == True:
#     pass
# else:
#     Chkbox_Cricket.click()



