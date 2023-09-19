from urllib import request

URL = "https://image.isu.pub/200611143019-a1dadf5b2575e7b48875e379a8f086bb/jpg/page_1.jpg"

response = request.urlretrieve(URL, "image.jpg")
