# Imports
from os import pardir
from bs4 import BeautifulSoup
import requests
import re

# Reading an HTML File
with open("Example_Html_Files/index2.html", "r") as f:
    doc = BeautifulSoup(
        f, "html.parser"
    )  # define doc as the file index1.html as a HTML file parsed by BeautifulSoup

tag = doc.find("option")
print(tag)

# modifying a tag
# tag['value'] = 'new value'
tag["selected"] = "False"

#######################
# adding an attribute
#######################

# tag[newattr] = 'new attr value'
# tag['color'] = 'blue

# print all tag attributes
print(tag.attrs)

##########################
# looking for class names
##########################
# Can't use class = as this is pre-used in Python for another function
# instead us class_=

tags = doc.find_all(class_="btn-item")  # find all items of class btn-item
print(tags)

################################
# finding regular expressions
################################

tags = doc.find_all(
    text=re.compile("\$.*")
)  # match the dollar sign and then anything after it, \$ used as $ alone is for a separate function
for tag in tags:
    print(tag.strip())  # prints removing the whitespace

################################################################
# regular expressions and limits, add limit after text criteria
################################################################

tags = doc.find_all(
    text=re.compile("\$.*"), limit=1
)  # match the dollar sign and then anything after it, \$ used as $ alone is for a separate function
for tag in tags:
    print(tag.strip())  # prints removing the whitespace

##################################################
# saving changes to document
##################################################

tags = doc.find_all(
    "input", type="text"
)  # match the dollar sign and then anything after it, \$ used as $ alone is for a separate function
for tag in tags:
    tag["placeholder"] = "I Changed You!"

with open("changed.html", "w") as file:  # open new file in write mode
    file.write(str(doc))
