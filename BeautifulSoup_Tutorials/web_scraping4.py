# Imports
from bs4 import BeautifulSoup
import requests
import re  # regular expression modules

#########################################
# Dynamic Input - What GPU do you want?
#########################################

search_term = input("what product do you want to search for?")

url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"

page = requests.get(url).text

doc = BeautifulSoup(page, "html.parser")

##########################################
# Determining the number of pages
##########################################
page_text = doc.find(class_="list")
# this outputs something of the form:
# <strong>1<!-- -->/<!-- -->4</strong>
# Want to split this out so we get the last entry after the /
page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])
# print(pages)
items_found = {}
for page in range(1, pages + 1):  # start at page 1 and increase by 1 each time
    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}"

    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    # as only want items from within a particular div, it makes sense to define it by the class
    div = doc.find(
        class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell"
    )
    items = div.find_all(
        text=re.compile(search_term)
    )  # matches with any items satisfying the search term in some form
    for item in items:  # want to get the name and price of each item
        # print(items)
        parent = item.parent
        # account for possibility that parent may not be <a> tag
        link = None
        if parent.name != "a":
            continue
        link = parent["href"]

        next_parent = item.find_parent(
            class_="item-container"
        )  # looks for any parent in the tree with the class name
        try:
            price = next_parent.find(class_="price-current").find("strong").string
            items_found[item] = {
                "price": int(price.replace(",", "")),
                "link": link,
            }  # create dictionary based on items found with price and item link
        except:
            pass

print(items_found)

# sort items found by price, OPTIONAL, just added this for sake of following the tutorial
sorted_items = sorted(items_found.items(), key=lambda x: x[1]["price"])

for item in sorted_items:
    print(item[0])  # print item name
    print(f"${item[1]['price']}")  # print item price with $ prefix
    print(item[1]["link"])  # print item link
    print("-------------------------------")
