#
# Selenium Tutorial 01
# Chromedriver Download - Make sure the version is appropriate!:
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# Move the extracted exe file to the desired location
# 
# Prerequisites:
# - Check pip is installed: cmd -> pip
# - install selenium: pip install selenium
# - download appropriate chromedriver from the link
#

import selenium # import selenium module (if installed) if it's not already there
from selenium import webdriver #import required webdriver module

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe" #define the chromedriver path for reference

driver = webdriver.Chrome(PATH) #define the driver exe's location to be used by the webdriver module

driver.get("https://techwithtim.net") #use the driver module to get a particular website

print(driver.title) # gets element returned by the web page
driver.quit() # close the browser