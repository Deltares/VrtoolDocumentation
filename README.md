# Veiligheidsrendement Documentation.

This is the repository containing all the user's  documentation related to the entire Veiligheidsrendement Suite (or `VrtoolSuite`). The `VrtoolSuite` is composed by the following repositories:

- [Veiligheidsrendement](https://github.com/Deltares/Veiligheidsrendement/) (or  `vrtool`).
    - Includes the database definition and a `ORM` wrapper.
- [Veiligheidsrendement Tools](https://github.com/Deltares/VrToolPreprocess) (or `vrtoolpreprocess`). A set of tools for pre- and post-processing data for the `vrtool`.
- Data Dashboard (to be defined).

# Project structure
```
VrtoolDocumentation
├── .config/
├── .github/
├── build/
└── vrtool_docs/
    ├── _static
    ├── _templates
    ├── conf.py
    └── index.rst
├── .gitignore
├── make.bat
├── Makefile
├── README.md
```

A quick look at what they mean:
* __.config/__ Contains the conda environment file to required to build using sphinx.
* __.github/__ Contains the workflows required by GitHub to build and deploy the documentation.
* __build/__ Output directory where `sphinx` will place the documentation __as a website__.
* __vrtool_docs/__ Source directory containing the documentation to be published.
    * This is where [documentation should be added](#how-to-write-documentation)
    * `conf.py` describes to `sphinx` how to build the website.
    * `index.rst` is the "welcome" page. 

# How to write documentation

We will be using [sphinx](https://www.sphinx-doc.org/en/master/) to generate our documentation written in [markdown language](https://markdown-it.github.io/). Extensions available for sphinx + markdown can be found in the [myst-parser](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html) documentation.

Steps to extend the current documentation using [GIT](https://git-scm.com/) with the command line (use [GitHub Desktop](https://desktop.github.com/) if you are not familiar with `GIT`):
0. [Install the repository locally](#install-the-repository).
1. Create your own branch (do not work under `main`).
    `git checkout -b docs/{{your_branch_name}}`
2. Extend the existing documentation in `vrtool_docs`. Tips:
    1. Try to cluster content within directories.
    2. Use descriptive names for the files. They are often used as "titles" in the Table of Contents.
3. Commit and push your changes regularly (to your own branch)
    1. `git add vrtool_docs\stability_screen_tutorial.md`
    2. `git commit -m "docs: Added new user tutorial for stability screen"`
    3. `git push`
4. Verify the documentation can still be built.
    1. Simply run `make html` in your console.
5. Create a pull-request via GitHub.
    1. Pull requests -> New pull request
    2. On the selector, the left side should be `base: main`, the right side your work branch:
        * `base: main` <- `compare: docs/{{your_branch_name}}`
    3. A review will be done on your branch, some changes might be requested.
    4. The issue is
6. Verify the published pages are correct.
    * __NOTE!__: The automatic build could have failed. Contact a project administrator if this happened.

# Install the repository.
Although not required, it is possible to checkout and install the repository locally to build and verify the documents prior to their publishing, we assume you are familiar and have installed [Anaconda](https://www.anaconda.com/download) or [miniconda](https://docs.conda.io/en/latest/miniconda.html). To do so, simply follow these steps from command line:

```bash
cd repos
git clone https://github.com/Deltares/VrtoolDocumentation.git
cd VrtoolDocumentation
conda env create -f .config\environment.yml -p .env\vrtooldocs_env
git checkout -b docs/{{your_branch_name}}
```

All `sphinx` dependencies should now be installed and you should be ready to run the `MAKE` file