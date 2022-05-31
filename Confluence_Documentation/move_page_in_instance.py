import os
from atlassian import Confluence
from dotenv import load_dotenv, find_dotenv
from numpy import append
import requests
import json

load_dotenv() 

def main():
    sourcePageId=""
    position="append"
    targetId=""
    test_url = f"https://{os.getenv('TARGET_SUBDOMAIN')}.atlassian.net/wiki/rest/api/content/{sourcePageId}/move/append/{targetId}"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {os.getenv('IFS_SANDBOX_CONFLUENCE_USERNAME')}:{os.getenv('IFS_SANDBOX_CONFLUENCE_PAT')}"
    }

    response = requests.put(test_url, auth=(os.getenv('IFS_SANDBOX_CONFLUENCE_USERNAME'), os.getenv('IFS_SANDBOX_CONFLUENCE_PAT')))

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

if __name__ == "__main__":
  main()