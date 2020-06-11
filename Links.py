from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://newtours.demoaut.com/")
print(driver.find_element_by_link_text("REGISTER").text)
print(driver.find_element_by_partial_link_text("SUPP").text)

All_Links = driver.find_elements_by_tag_name("a")
print("Total links are:", len(All_Links) )

links_list = []

for all_link in All_Links: #  print (all_link.text)
    links_list.append(all_link.text)

print(links_list)

#Links r working or not
for links in links_list:
    driver.find_element_by_link_text(links).click()
    print(driver.title)
    driver.back()

