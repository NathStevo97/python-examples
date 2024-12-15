#
# Selenium Tutorial 02 - Accessing Elements
# Chromedriver Download - Make sure the version is appropriate!:
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# Move the extracted exe file to the desired location
#
# Prerequisites:
# - Check pip is installed: cmd -> pip
# - install selenium: pip install selenium
# - download appropriate chromedriver from the link
#

import selenium  # import selenium module (if installed) if it's not already there
from selenium import webdriver  # import required webdriver module
from selenium.webdriver.common.keys import (
    Keys,
)  # grants access to text-based operations with html elements

# selenium webdriver imports to allow for explicit waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time  # allow for sleep commands for observability

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"  # define the chromedriver path for reference

driver = webdriver.Chrome(
    PATH
)  # define the driver exe's location to be used by the webdriver module

driver.get(
    "https://techwithtim.net"
)  # use the driver module to get a particular website

# From here elements can be accessed for Selenium to use
# Elements can be accessed via any of the following:
# id
# class
# value
# tag
# First three are most common, generally go id -> name -> class
# Class returns ONLY the first element found within the page matching that class name

search = driver.find_element_by_name("s")  # identify search bar and assign to variable
search.send_keys("test")  # input test text to search bar element
search.send_keys(Keys.RETURN)  # hit enter in search bar

time.sleep(5)  # pause for observability purposes

# Obtaining all search results from the first page
# Within the page, inspect the code again, from here you can start to understand how
# you can formulate the query

# One problem that arises is that if the element loaded takes a long time to load,
# it's better to have selenium wait until the full value is returned before it moves on as an error may occur

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "main")
        )  # wait until the prescence of the element of id = main is found before proceeding
    )
    # Want to search for all the headers of the search results
    # All within article tags, within a div called entry header and entry title

    articles = main.find_elements_by_tag_name(
        "article"
    )  # identify all articles elements in the main element
    for article in articles:
        header = article.find_element_by_class_name(
            "entry-summary"
        )  # find the entry title element for each article element
        print(header.text)
    # print(main.text) # print all text associated with the id = main element
except:
    driver.quit()  # if the try doesn't work, exit

time.sleep(5)

# print(driver.page_source) # print the entire page's code

# print(driver.title) # gets element returned by the web page
# driver.quit() # close the browser
