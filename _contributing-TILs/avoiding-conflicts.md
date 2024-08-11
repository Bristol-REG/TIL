# How to push/pull without conflicts

Because a [GitHub Action](/.github/workflows/build.yml) runs and adds commits to the repo, you will probably find that you can't push to the repo without first pulling the changes.

> [!TIP]  
> Remember to pull from GitHub before you make any changes or commits. You should also avoid committing changes to the [`README.md`](/README.md) file, as this will get updated automatically by GitHub Actions and if you update it too then you can easily get merge conflicts.

If you are editing locally and forget to pull from GitHub before making a commit, then you can subsequently pull changes from GitHub, asking for Git to rebase your changes onto the newly pulled commits. Then you can push your changes to GitHub. If you also have [previewed what the `README.md` will look like](preview-README.md) after the GitHub Action has run, you should discard those changes first.

The commands will look similar to the following:

```bash
git add my-topic/my-new-TIL.md
git commit -m "Add a TIL about something I learned"
git restore README.md  # (optional) discard any changes to README.md, if you have changed it
git pull --rebase
git push
```

If you have also committed changes to [`README.md`](/README.md) then this approach won't work and you'll probably get a merge conflict. Don't worry, just edit the file locally to remove the conflict, and make a new commit to merge the 'branches' back together again.
