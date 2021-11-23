import os
from atlassian import Confluence
from dotenv import load_dotenv, find_dotenv

load_dotenv() 

def main():
    confluence = Confluence(
        url=os.getenv('url'),
        username=os.getenv('uname'),
        password=os.getenv('password'),
        cloud=os.getenv('cloud')
    )
    #print(confluence.url)
    #print(confluence.username)
    #print(confluence.password)
    #print(confluence.cloud)

    #test = confluence.create_page(
    #    space='TDA',
    #    title='Test Page 1',
    #    body='This is a test page please ignore!'
    #)

if __name__ == "__main__":
  main()