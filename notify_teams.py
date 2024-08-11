"""
Send a notification to MS Teams with a list of new TILs added to the repository.
"""

import os
import sys
from pathlib import Path
from textwrap import shorten

import git
import requests


def get_added_files(repo_path: str | Path, commit1: str, commit2: str) -> list[str]:
    """
    Get files that were added between two commits.

    Args:
        commit1: The hash of the earlier commit.
        commit2: The hash of the later commit.

    Returns:
        List of the file paths that were added.
    """
    repo = git.Repo(repo_path)
    diff = repo.commit(commit1).diff(commit2, paths="*.md")
    return [
        file.b_path
        for file in diff
        if file.change_type in ("A") and not file.b_path.endswith("README.md")
    ]


def get_files_markdown(repo_url: str, added_files: list[str]) -> str:
    """
    Get the markdown list of added files.

    Args:
        repo_url: The URL to the repository on GitHub, e.g. https://github.com/owner/repo.
        added_files: The list of file paths that were added.

    Returns:
        The markdown list of added files, with links to the files on GitHub and a excerpt of their
        content.
    """
    files_markdown = ""
    for file in added_files:
        url = f"{repo_url}/blob/main/{file}"
        with Path(file).open() as f:
            title = f.readline().lstrip("#").strip() or deslugify(path.stem)
            excerpt = shorten(f.read(200), 100, placeholder="...")
        files_markdown += f"- [{title}]({url})\n  {excerpt}\n"
    return files_markdown


def prepare_json(repo_url: str, added_files: list[str]) -> dict:
    """
    Prepare the JSON payload for sending an MS Teams Adaptive Card notification.

    Args:
        repo_url: The URL to the repository on GitHub, e.g. https://github.com/owner/repo.
        added_files: The list of file paths that were added.

    Returns:
        The JSON payload for the MS Teams Adaptive Card.
    """
    return {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "contentUrl": None,
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": "New TILs",
                            "weight": "Bolder",
                            "size": "Large",
                        },
                        {
                            "type": "TextBlock",
                            "text": get_files_markdown(repo_url, added_files),
                            "wrap": True,
                        },
                    ],
                },
            }
        ],
    }


def send_teams_notification(webhook_url: str, payload: dict) -> None:
    """
    Send an Adaptive Card notification to an MS Teams webhook URL.

    Args:
        webhook_url: The URL to the MS Teams webhook.
        payload: The JSON payload containing an MS Teams Adaptive Card.
    """
    response = requests.post(webhook_url, json=payload)
    response.raise_for_status()


def deslugify(slug: str) -> str:
    """
    Convert a slug to a human-readable title.

    Args:
        slug: The slug to convert.

    Returns:
        The human-readable title.
    """
    slug = slug.replace("-", " ").replace("_", " ").strip()
    return slug[:1].upper() + slug[1:]  # Capitalise the first letter and leave the rest as-is


if __name__ == "__main__":
    added_files = get_added_files(
        repo_path=Path(__file__).parent, commit1=sys.argv[1], commit2=sys.argv[2]
    )
    if added_files:
        payload = prepare_json(
            repo_url=os.environ["GITHUB_SERVER_URL"] + "/" + os.environ["GITHUB_REPOSITORY"],
            added_files=added_files,
        )
        send_teams_notification(os.environ["TEAMS_WEBHOOK_URL"], payload)
        print("New TILs. Notification sent.")
    else:
        print("No new TILs. No notification required.")
