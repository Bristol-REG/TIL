# How to preview the `README.md` locally

> [!NOTE]
> For normal use, you don't need to do this. A [GitHub Action](/.github/workflows/build.yml) will automatically update the `README.md` file when you push changes to the repo.
>
> Also bear in mind that you probably don't want to commit changes to the [`README.md`](/README.md), unless you are updating some of the the parts outside the placeholder tags. Otherwise you will likely get merge conflicts. See below for how to discard changes to the file before pulling.

To build the [`README.md`](/README.md) file locally, you will need to create and activate a virtual environment using Python 3.12+, and then install the dependencies for this project.

For Mac/Linux:

```bash
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

For Windows:

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

You can then run the `generate_readme.py` script to see what the new [`README.md`](/README.md) file will look like.

```bash
python generate_readme.py
```

It might be helpful to discard uncommitted changes to the [`README.md`](/README.md) file before pulling from GitHub, to avoid merge conflicts. You can do this with the following command:

```bash
git restore README.md
```
