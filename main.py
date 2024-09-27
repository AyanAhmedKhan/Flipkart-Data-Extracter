from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
file=0

query=input("Enter the product\n")
if query in ["mobile", "laptop"]:
    class_name = "tUxRFH"
else:
    class_name = "slAVV4"

driver=webdriver.Chrome()

for i in range(1,20):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
    elems=driver.find_elements(By.CLASS_NAME, class_name)
    print(f"{len(elems)} item found")
    for elem in elems:
        d= elem.get_attribute("outerHTML")
        with open (f"data/{query}_{file}.html","w", encoding='utf-8') as f:
         f.write(d)
         file+=1
    time.sleep(1)
driver.close()
