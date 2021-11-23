# Confluence_Documentation
Repo developed as part of research for working with Confluence documentation, managing pages and transferring pages from a markdown-based wiki e.g. Azure DevOps to Confluence's own format.

---

## Prerequisites

1. Install required modules:
```
pip install -r .\requirements.txt
```

2. Create .env file in root directory and add the following:
```
url='https://your-domain.atlassian.net'
username=jira_username
password=jira_api_token
cloud=True/False
```

To get the API token, one can follow the instructions outlined [here](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html)