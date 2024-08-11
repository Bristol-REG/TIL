# How to contribute a TIL

> [!TIP]  
> TIL stands for "today I learned". We constantly learn new things that would be for others (including our future self!) to see.

TILs are short markdown files that live inside a directory named after the topic of the TIL.

For first-time contributors, it is recommended that you use the GitHub web interface to add new TILs, which avoids pulling/pushing and the potential for merge conflicts. If you will be editing locally, see the advice on [avoiding conflicts](avoiding-conflicts.md). 

The title of the TIL should be a short, descriptive phrase that summarises the content of the TIL. The title should be a level 1 heading on the very first line of the TIL. For example:

```markdown
# This is the heading

This is the text of the TIL...
```

Feel free to include code snippets, links to resources, or any other information that you think would be useful to someone else.

Don't worry about including your name or a date, we can get this from the Git history.

After creating a TIL, commit and push your changes back to GitHub. If you have push access to this repo, then that's all you'll need to do. If you are an external collaborator (we thank you for contribution!) then you'll need to create a pull request.

Your contribution will be considered public domain ([CC0](LICENSE)) unless otherwise noted. Any referenced content may have its own license.

After you push to the repo (or your pull request is merged), a [GitHub Action](/.github/workflows/build.yml) will automatically add your TIL, along with the date it was created, to the [`README.md`](/README.md) for this repo.
