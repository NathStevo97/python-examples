# Tutorial 04 - Action Chains
# Documentation link: 
import selenium # import selenium module (if installed) if it's not already there
from selenium import webdriver #import required webdriver module
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe" #define the chromedriver path for reference

driver = webdriver.Chrome(PATH) #define the driver exe's location to be used by the webdriver module
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5) # wait 5 seconds before continuing

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
upgrades = [driver.find_element_by_id("productPrice" + str(i)) for i in range (1, -1, -1)] # checks the upgrades for each id productPrice0, 1, 2, etc

actions = ActionChains(driver) #Action chains work in a similar manner to an event queue
actions.click(cookie) # click based on mouse location
for i in range(5000):
    actions.perform() # perform all stored actions
    count = int(cookie_count.text.split(" ")[0]) # takes the cookie count element and extracts the first part of the element's text before the " "
    print(count)
    for item in upgrades:
        value = int(item.text)
        if value <= count: # if the value of the upgrade is less than or equal to the total count, run the following
            upgrade_actions = ActionChains(driver)
            upgrade_actions.click() # click on the particular upgrade item to upgrade accordingly
            upgrade_actions.perform()
