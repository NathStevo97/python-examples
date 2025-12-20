# Goal of this section, want to get the elements in tbody
# Imports
from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"  # define url to be searched
result = requests.get(
    url
).text  # use request module to list url content as text to be parsed
doc = BeautifulSoup(result, "html.parser")  # parse url text using BS4s HTML parser

tbody = doc.tbody
# print(tbody)

# Want to navigate by viewing the elements on the same level of the html tree
# could get all the contents of <tbody> and loop through
# in this case, want to navigate by looking through the siblings of each row in the tbody element

trs = tbody.contents  # gives a list of all the tags in tbody (table rows)
# print(trs)

print(trs[0].next_sibling)  # print the next entry / sibling down from trs[0]
print(trs[1].previous_sibling)  # print previous sibling
print(list(trs[0].next_siblings))  # list all the table rows after tr[0]

# parents
print(trs[0].parent)  # get parent tag to trs
print(trs[0].parent.name)  # get name of parent tag to trs
print(list(trs[0].descendants))  # get descendants of trs, in this case the table data
# could also use .contents or .children, latter gives tags only

prices = {}  # define empty dictionary to be added
for tr in trs[
    :10
]:  # for each entry in table rows (trs) up to 10th entry (would need to deal with "none" situations in future scenarios e.g look for a dollar sign and work from there)
    name, price = tr.contents[2:4]  # want to get just the name and price
    fixed_name = name.p.string
    print(
        fixed_name
    )  # name is inside of a p tag, so can just get that and print the string
    fixed_price = price.a.string
    print(fixed_price)  # price in <a> tag, get string

    prices[
        fixed_name
    ] = fixed_price  # append to prices {} with key being fixed name and value being fixed prices

print(prices)
