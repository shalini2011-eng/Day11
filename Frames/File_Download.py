from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os.path

# Save files in desired location
chromeoptions=Options()
chromeoptions.add_experimental_option("prefs",{"download.default_directory":"C:\Downloadedfiles"})
######
driver=webdriver.Chrome(chrome_options=chromeoptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

# Download text file
driver.find_element_by_id("textbox").send_keys("welcome") # text box/area
driver.find_element_by_id("createTxt").click() # Generate button
driver.find_element_by_id("link-to-download").click() # Download link
time.sleep(5)

if os.path.exists("C:\Downloadedfiles\info.txt")==True:
    print("text File Exists")
else:
    print("text File Not Exists")

# Download pdf file
driver.find_element_by_id("pdfbox").send_keys("welcome123")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()
time.sleep(5)
if os.path.exists("C:\Downloadedfiles\info.pdf")==True:
    print("pdf File Exists")
else:
    print("pdf File Not Exists")
