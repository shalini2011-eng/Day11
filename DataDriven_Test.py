from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from XLUtils import *
from selenium.webdriver import ActionChains
import openpyxl

driver = webdriver.Chrome()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

element = driver.find_element_by_xpath("//input[@id='principal']")
driver.execute_script("arguments[0].scrollIntoView();",element)

file_name = 'D:\Download_Python_File\Login_File.xlsx'
sheet = 'TestData'
rows = getRowCount(file_name, sheet)
print(rows)
columns =getColumnCount(file_name,sheet)
print(columns)

#print(readData(file_name, sheet, rows, columns))
for r in range(2, rows+1):
    driver.find_element_by_xpath("//input[@id='principal']").send_keys(readData(file_name, sheet, r, 1))
    driver.find_element_by_xpath("//input[@id='interest']").send_keys(readData(file_name, sheet, r, 2))
    driver.find_element_by_xpath("//input[@id='tenure']").send_keys(readData(file_name, sheet, r, 3))
    Period_Drpd = Select(driver.find_element_by_xpath("//select[@id='tenurePeriod']"))
    Period_Drpd.select_by_visible_text(readData(file_name, sheet, r, 4))
    Freq_drpd= Select(driver.find_element_by_xpath("//select[@id='frequency']"))
    Freq_drpd.select_by_visible_text(readData(file_name, sheet, r, 5))
    driver.find_element_by_xpath("//div[@class='PT25']//a[1]//img[1]").click()

    Maturity_Actual_Value = driver.find_element_by_xpath("//span[@id='resp_matval']").text
    writeData(file_name, sheet, r, 7, Maturity_Actual_Value)

    Maturity_Expected_Value = readData(file_name, sheet, r, 6)

    if float(Maturity_Expected_Value) == float(Maturity_Actual_Value):
        print("Test passed")
        writeData(file_name, sheet, r, 8, 'Pass')
    else:
        print("Test failed")
        writeData(file_name, sheet, r, 8, 'Fail')

    driver.find_element_by_xpath("//img[@class='PL5']").click()#clear values

driver.close()







