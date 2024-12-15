from platform import python_implementation
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()


def main():
    # Source Instance Configuration
    sourceSpaceKey = ""
    sourcePageId = ""
    source_url = f"https://{os.getenv('SOURCE_SUBDOMAIN')}.atlassian.net/wiki/rest/api/content/{sourcePageId}?expand=history, version, body"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('NATHAN_PERSONAL_CONFLUENCE_USERNAME')}:{os.getenv('NATHAN_PERSONAL_CONFLUENCE_PAT')}",
    }

    # Get source page content
    source_response = requests.get(
        source_url,
        headers=headers,
        auth=(
            os.getenv("NATHAN_PERSONAL_CONFLUENCE_USERNAME"),
            os.getenv("NATHAN_PERSONAL_CONFLUENCE_PAT"),
        ),
    )

    # Define target payload from source response
    json_payload = json.dumps(
        json.loads(source_response.text),
        sort_keys=True,
        indent=4,
        separators=(",", ": "),
    )
    print(json_payload)

    # target configuration
    targetSpaceKey = "~"
    target_url = (
        f"https://{os.getenv('TARGET_SUBDOMAIN')}.atlassian.net/wiki/rest/api/content"
    )
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('IFS_SANDBOX_CONFLUENCE_USERNAME')}:{os.getenv('IFS_SANDBOX_CONFLUENCE_PAT')}",
    }


if __name__ == "__main__":
    main()
