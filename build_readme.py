"""
Build a README.md file with a table of contents and links to all of the markdown files in the
repository.

The TILs are grouped by topic. Topics and TILs are sorted alphabetically, except those whose paths
start with an underscore (_) which are sorted to the top of the list.

The README.md file is expected to have the following placeholders:

    <!-- toc starts -->
    <!-- toc ends -->

and

    <!-- index starts -->
    <!-- index ends -->

If the README.md file does not exist, it will be created. If the placeholders for the table of
contents and index of links do not exist, they will be added.

This script was inspired by the TILs of [Lacey Henschel](https://github.com/williln/til) and [Simon
Willison](https://github.com/simonw/til).
"""

import datetime
import re
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import git


def get_created_times(
    repo_path: str | Path, ref: str = "main"
) -> dict[str, datetime.date]:
    """
    Get the first commit date for each file in the repository.

    Args:
        repo_path: The path to the root of the repository.
        ref: The branch or commit to start from.

    Returns:
        A dictionary with the file paths as keys and the first commit date as values.
    """
    created_times = {}
    repo = git.Repo(repo_path)
    commits = reversed(list(repo.iter_commits(ref)))
    for commit in commits:
        date = commit.committed_datetime.date()
        changed_files = list(commit.stats.files.keys())
        for filepath in changed_files:
            if filepath not in created_times:
                created_times[filepath] = date
    return created_times


def get_by_topic(
    repo_path: str | Path, created_times: dict[str, datetime.date]
) -> dict[tuple[str], dict[str, dict]]:
    """
    Build a dictionary of all the markdown files in the repository, with their title and created
    date, grouped by topic.

    Exclude any file named README.md and all top-level markdown files.

    Args:
        repo_path: The path to the root of the repository.
        created_times: A dictionary with the file paths as keys and the first commit date as values.

    Returns:
        A dictionary with the topics as keys, and a dictionary of files as values. Each file
        dictionary has its path as the key, and a dictionary with the title and created date as
        values.
    """
    by_topic = defaultdict(dict)
    for file in Path(repo_path).glob("*/**/*.md"):
        file = file.relative_to(repo_path)
        if file.name == "README.md" or any(part.startswith(".") for part in file.parts):
            continue
        topic = deslugify(file.parts[0:-1])
        with file.open() as f:
            title = f.readline().lstrip("#").strip() or deslugify(file.stem)
        by_topic[topic][file] = {
            "title": title,
            "created": created_times.get(str(file)),
        }

    # Ensure that all intermediate topics are present
    # e.g. if there is by_topic[Path('One')]
    #              and by_topic[Path('One/Two/Three')]
    # then also create by_topic[Path('One/Two')]
    intermediate_topics = {
        topic[:i] for topic in by_topic.keys() for i in range(1, len(topic))
    }
    for topic in intermediate_topics:
        by_topic.setdefault(topic, {})

    return by_topic


def render_toc(by_topic: dict[tuple[str], dict[str, dict]]) -> str:
    """
    Render a table of contents for the README.md file, with bookmark links to each topic.

    Topics are sorted alphabetically, except those whose paths start with an underscore (_) which
    are sorted to the top of the list.

    Args:
        by_topic: A dictionary with the topics as keys, and a dictionary of files as values. Each
            file dictionary has its path as the key, and a dictionary with the title and created
            date as values.

    Returns:
        The markdown for the table of contents.
    """
    index = []
    for topic in sorted(by_topic):
        # Topics starting with an underscore (_) are sorted first
        name = topic[-1].lstrip("_")
        bookmark = get_bookmark(topic)
        indent_depth = "    " * (len(topic) - 1)
        index.append(f"{indent_depth}- [{name}](#{bookmark})")
    return "\n".join(index).strip()


def render_index(by_topic: dict[tuple[str], dict[str, dict]]) -> str:
    """
    Render an index of links to each markdown file in the repository, grouped by topic.

    Topics and TILs are sorted alphabetically, except those whose paths start with an underscore (_)
    which are sorted to the top of the list.

    Args:
        by_topic: A dictionary with the topics as keys, and a dictionary of files as values. Each
            file dictionary has its path as the key, and a dictionary with the title and created
            date as values.

    Returns:
        The markdown for the index of links.
    """
    toc = []

    def sort_by_sticky_then_title(dict_items):
        path, info = dict_items
        return -path.stem.startswith("_"), info["title"]

    for topic, files in sorted(by_topic.items()):
        # Topics starting with an underscore (_) are sorted first
        name = topic[-1].lstrip("_")
        bookmark = get_bookmark(topic)
        heading_level = "#" * (len(topic) + 2)
        toc.append(f'{heading_level} {name} <a id="{bookmark}"></a>\n')
        for path, info in sorted(files.items(), key=sort_by_sticky_then_title):
            list_item = f"- [{info['title']}]({path})"
            if info["created"]:
                list_item += f" - {info['created']}"
            toc.append(list_item)
        toc.append("")
    return "\n".join(toc).strip()


def update_readme(
    repo_path: str | Path, toc_markdown: str, index_markdown: str
) -> None:
    """
    Update the README.md file at the root of the repository with a table of contents and index of
    links.

    The README.md file is expected to have the following placeholders:

        <!-- toc starts --><!-- toc ends -->
        <!-- index starts --><!-- index ends -->

    If the README.md file does not exist, it will be created. If the placeholders for the table of
    contents and index of links do not exist, they will be added.

    Args:
        repo_path: The path to the root of the repository. toc_markdown: The markdown for the table
            of contents.
        index_markdown: The markdown for the index of links.
    """
    readme_path = Path(repo_path) / "README.md"
    readme_path.touch()
    readme_content = readme_path.read_text()

    toc_pattern = re.compile(
        r"<!\-\- toc starts \-\->.*<!\-\- toc ends \-\->", re.DOTALL
    )
    index_pattern = re.compile(
        r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL
    )

    toc_markdown = f"<!-- toc starts -->\n{toc_markdown}\n<!-- toc ends -->"
    index_markdown = f"<!-- index starts -->\n{index_markdown}\n<!-- index ends -->"

    if toc_pattern.search(readme_content):
        readme_content = toc_pattern.sub(toc_markdown, readme_content)
    else:
        readme_content += toc_markdown

    if index_pattern.search(readme_content):
        readme_content = index_pattern.sub(index_markdown, readme_content)
    else:
        readme_content += index_markdown

    readme_path.write_text(readme_content)


def deslugify(slugs: Iterable[str]) -> tuple[str]:
    """
    Convert slugs to human-readable titles.

    Args:
        slugs: The slugs to convert.

    Returns:
        The human-readable titles.
    """
    titles = []
    for slug in slugs:
        title = slug.replace("-", " ").replace("_", " ").strip()
        title = (
            title[:1].upper() + title[1:]
        )  # Capitalise the first letter and leave the rest as-is
        titles.append(title)
    return tuple(titles)


def get_bookmark(topic: tuple[str]) -> str:
    """
    Generate a valid HTML link hash (or bookmark) from a topic tuple.
    """
    return "--".join(
        part.lstrip("_").lower().replace(" ", "-").replace("'", "").replace('"', "")
        for part in topic
    )


if __name__ == "__main__":
    repo_path = Path(__file__).parent.resolve()
    times = get_created_times(repo_path)
    by_topic = get_by_topic(repo_path, times)
    toc = render_toc(by_topic)
    index = render_index(by_topic)
    update_readme(repo_path, toc, index)
