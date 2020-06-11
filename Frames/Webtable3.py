from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

username = driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("admin")
password = driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
#driver.find_element_by_xpath("//*[@id='btnLogin']")
driver.find_element_by_xpath("//input[@id='btnLogin']").click()

admin = driver.find_element_by_xpath("//b[contains(text(),'Admin')]")
userManagement = driver.find_element_by_xpath("//a[@id='menu_admin_UserManagement']")
users =driver.find_element_by_xpath("//a[@id='menu_admin_viewSystemUsers']")
action = ActionChains(driver)
action.move_to_element(admin).move_to_element(userManagement).move_to_element(users).click().perform()

#table = driver.find_element_by_xpath("//table[@id='resultTable']")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

NoOfRows = len(driver.find_elements_by_xpath("//table[@id='resultTable']//tbody/tr"))
NoOfCols = len(driver.find_elements_by_xpath("//table[@id='resultTable']//tbody/tr[1]/td"))

print(NoOfRows)
print(NoOfCols)

for r in range(1,NoOfRows+1):
    for c in range(2,NoOfCols+1):
        value = driver.find_element_by_xpath("//table[@id='resultTable']//tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end='   ')
    print()


count = 0
for r in range(1,NoOfRows+1):
        value = driver.find_element_by_xpath("//table[@id='resultTable']//tbody/tr["+str(r)+"]/td[5]").text

        if value == "Enabled":
            count = count+1

print("Enabled users are", count)
disabled_users = NoOfRows-count
print("Disabled users are", disabled_users)
print("total users are", count+disabled_users)






