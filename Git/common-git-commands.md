# Commonly used commands in Git

- `git clone REPO_URL`

- `git status`: Show status of files. useful for picking up ones you've forgotten to add/ignore.

- `git diff`

    - `git diff --name-only`: Show the files that you've changed, but only their names (useful for the next bit).

    - `git diff --staged`: Show the changed that you've already staged with `git add`.

- `git add FILENAME`

    - `git add -A`: Stage all changes, including files not yet in the repo.

- `git commit`

    - `git commit -a`: Commit all modified/deleted files without having to add them first.

    - `git commit -m "message here"`: Use the the provided message without opening an editor.

- `git log`: Show previous commit messages. Useful if you forgot if you pushed the last commit or not.

    - `git log --graph`: Show a graph/timeline of different commits.

    - `git log --oneline`: Show only the first line of the commit messages (fit more commits on the screen).

    - `git log --all`: Show all branches.

- `git restore FILENAME`: Discard any changes you've made, going back to the most recently committed version of a file. (This is a newer command. On older versions of Git you can do `git checkout FILENAME`.)

- `git switch BRANCH`: Change branch. (This is a newer command. On older versions of Git you can do `git checkout BRANCH`.)

- `git push`

- `git pull`

    - `git pull --rebase`: Pull changes, but try to rewrite your local commits instead of making a merge commit.

# Further help

Julia Evans has put together a nice [Git Cheat Sheet](https://wizardzines.com/comics/git-cheat-sheet/).

Also see: https://ohshitgit.com/

Via: [Richard](https://github.com/richard-lane), [Léo](https://github.com/l-gorman) and [James](https://github.com/jatonline)
