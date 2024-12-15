# Imports
from os import pardir
from bs4 import BeautifulSoup
import requests

# Reading an HTML File
with open("Example_Html_Files/index1.html", "r") as f:
    doc = BeautifulSoup(
        f, "html.parser"
    )  # define doc as the file index1.html as a HTML file parsed by BeautifulSoup

# print doc with indentations
# print(doc.prettify())

# finding elements by tags
tag = doc.title
print(tag)

# find string associated with tag
tag = doc.title
print(
    tag.string
)  # Note: if tag or tag.string was changed in value, this would be updated in the doc too!

# find all tags of a particular parameter (find all by tag name)
tags = doc.find_all("p")
print(tags)

# accessing nested tags, this is using the preset variable tags
tags = doc.find_all("p")[0]
print(tags.find_all("b"))  # finds all elements with <b> tag in tags


# Using BS4 with an HTML Website
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"  # define url of choice
result = requests.get(
    url
)  # result obtained by the requests module making a get request to url

doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify)

# In this example need to look for $ appearing
prices = doc.findAll(text="$")
print(prices)

# given the above, this just prints out the dollar sign associated with the price, not helpful!
# BS4's tree structure can be leveraged here, and the $ can be used to find the "parent" location
# When reading in an html doc, a tree structure is followed e.g. <TITLE> is a child of the <HEAD> tag

parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)
