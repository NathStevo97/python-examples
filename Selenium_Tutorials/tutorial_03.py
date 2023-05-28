# Tutorial 03 - Page Navigation: Clicking buttons, switching pages, etc

import selenium # import selenium module (if installed) if it's not already there
from selenium import webdriver #import required webdriver module
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe" #define the chromedriver path for reference

driver = webdriver.Chrome(PATH) #define the driver exe's location to be used by the webdriver module

driver.get("https://techwithtim.net/") #use the driver module to get a particular website

link = driver.find_element_by_link_text("Python Programming") # finds html element based on the text that appears with the link

link.click() # click the link based on the element found in the above variable

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials")) # wait until the prescence of the element of id = main is found before proceeding
    ) # Wait until prescence of element is detected
    element.click() # click the button

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003")) # wait until the prescence of the element of id = main is found before proceeding
    ) # Wait until prescence of element is detected
    element.click()

    driver.back() # skip back 1 page
    #driver.back()
    #driver.back()
    driver.forward() # skip forward 1 page
    #driver.forward()
    #driver.forward()

except:
    driver.quit() # if the try doesn't work, exit

driver.quit()

#Note: element.clear() should be used with elements such as a search bar to remove any preexisting text