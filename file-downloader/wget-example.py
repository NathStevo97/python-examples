import wget

URL = "https://bellard.org/bpg/2.png"

response = wget.download(URL, "image.png")
