from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os.path

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"D:\Download_Python_File"})

driver = webdriver.Chrome(options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#Download Text File
driver.find_element_by_xpath("//textarea[@id='textbox']").send_keys("Shalini text file2")
driver.find_element_by_xpath("//button[@id='createTxt']").click()
driver.find_element_by_xpath("//a[@id='link-to-download']").click()
time.sleep(5)
if os.path.exists("D:\Download_Python_File\info.txt") == True:
    print("file downloaded successfully")
else:
    print("file doesn't exist")

driver.find_element_by_xpath("//textarea[@id='pdfbox']").send_keys("Shalini pdf file for python")
driver.find_element_by_xpath("//button[@id='createPdf']").click()
driver.find_element_by_xpath("//a[@id='pdf-link-to-download']").click()
time.sleep(5)
if os.path.exists("D:\Download_Python_File\info.pdf") == True:
    print("pdf file downoaded sucessfully")
else:
    print("pdf file not downloaded")

time.sleep(5)
driver.close()

