import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()


def main():
    # Source Instance Configuration
    sourceSpaceKey = ""
    source_url = f"https://{os.getenv('SOURCE_SUBDOMAIN')}.atlassian.net/wiki/rest/api/space/{sourceSpaceKey}/content"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('NATHAN_PERSONAL_CONFLUENCE_USERNAME')}:{os.getenv('NATHAN_PERSONAL_CONFLUENCE_PAT')}",
    }
    print(source_url)
    print(headers)
    # Get source space content
    source_response = requests.get(
        source_url,
        headers=headers,
        auth=(
            os.getenv("NATHAN_PERSONAL_CONFLUENCE_USERNAME"),
            os.getenv("NATHAN_PERSONAL_CONFLUENCE_PAT"),
        ),
    )

    payload = json.dumps(
        json.loads(source_response.text),
        sort_keys=True,
        indent=4,
        separators=(",", ": "),
    )
    print(payload)

    # Target Confluence Configuration

    targetSpaceKey = ""
    target_url = (
        f"https://{os.getenv('TARGET_SUBDOMAIN')}.atlassian.net/wiki/rest/api/content"
    )
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('IFS_SANDBOX_CONFLUENCE_USERNAME')}:{os.getenv('IFS_SANDBOX_CONFLUENCE_PAT')}",
    }

    print(target_url)
    print(headers)

    # POST Request to Target Confluence Instance


if __name__ == "__main__":
    main()
