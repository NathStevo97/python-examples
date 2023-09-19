# Import the requests library
import requests

URL = "https://image.isu.pub/200611143019-a1dadf5b2575e7b48875e379a8f086bb/jpg/page_1.jpg"

#  Download the data behind the URL
response = requests.get(URL)

#  Open the response generated into a new file in your local called image.jpg
open("image.jpg", "wb").write(response.content)
