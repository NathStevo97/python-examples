#https://atlassian-python-api.readthedocs.io/confluence.html#get-page-info
#https://developer.atlassian.com/server/confluence/confluence-rest-api-examples/

import requests
import json
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv() 

# Login & Authenticate to Desired Space

# Source Instance Configuration
sourceSpaceKey = ""
sourcePageId= ""
source_url = f"https://{os.getenv('SOURCE_SUBDOMAIN')}.atlassian.net/wiki/rest/api/content/{sourcePageId}?expand=body.storage"

# Get desired page & Content
headers = {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": f"Bearer {os.getenv('USERNAME')}:{os.getenv('CONFLUENCE_PAT')}"
   }
   
   # Get source page content
   source_response = requests.get(
      source_url,
      headers=headers,
      auth=(os.getenv('CONFLUENCE_USERNAME'), os.getenv('CONFLUENCE_PAT'))
   )


# Check page content to see if it contains a azure link
# i.e. https://dev.azure.com/ifs-ale/IFS Cloud/_wiki/wikis/IFS-Cloud.wiki/*/*

# Find associated page based on last part of original URL (variablise)
# Replace any _ in above with +
# Find page ID of page with title defined above

# Create new url https://ifsdev.atlassian.net/wiki/spaces/IFSCLOUD/pages/<PAGE ID>/<NEW TITLE>

# Update appropriate URL in content to match