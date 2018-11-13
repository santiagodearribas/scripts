#import time
#print("running")
#time.sleep(5000)

#import os

import selenium 
from selenium import webdriver
#os.environ["webdriver.chrome.driver"] = chromedriver

url = "https://login.dcu.ie/idp/profile/SAML2/Redirect/SSO?execution=e1s1"
path = r'H:\chromedriver.exe'

driver = webdriver.Chrome(path)

driver.get(url)
s = driver.find_element_by_name("username")
p = driver.find_element_by_name("password")
s.send_keys("16449272")
p.send_keys("63d8uxgd")
	
login = driver.find_element_by_class_name("form-element form-button")
login.click()
