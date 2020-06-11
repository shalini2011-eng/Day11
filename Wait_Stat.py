from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

driver = webdriver.Chrome()
#driver.implicitly_wait(10)

wait =WebDriverWait(driver, 10, 2, ignored_exceptions=[NoSuchElementException,ElementNotSelectableException,ElementNotVisibleException])

driver.get("https://www.google.com/")
searchbox = driver.find_element_by_name("q")
searchbox.send_keys("Selenium")
searchbox.send_keys(Keys.ENTER)

searchlink = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text() ='Selenium']")))
#driver.find_element_by_xpath("//h3[text() ='Selenium']").click()
searchlink.click()



#
# seachbox.send_keys("Selenium")
# searchbox.submit()


