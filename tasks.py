#!/usr/bin env python
"""Project automation code using Invoke.py as replacement for `make`."""

import os
import webbrowser
from urllib.request import pathname2url

from invoke import task

PIPENV_RUN = "pipenv run"
PACKAGE_NAME = 'db_tools'


def browser(path):
    webbrowser.open("file://" + pathname2url(os.path.abspath(path)))


@task
def clean_build(ctx):
    """Remove build artifacts."""
    ctx.run("rm -fr build/")
    ctx.run("rm -fr dist/")
    ctx.run("rm -fr .eggs/")
    ctx.run("find . -name '*.egg-info' -exec rm -fr {} +")
    ctx.run("find . -name '*.egg' -exec rm -f {} +")


@task
def clean_pyc(ctx):
    """Remove Python file artifacts."""
    ctx.run("find . -name '*.pyc' -exec rm -f {} +")
    ctx.run("find . -name '*.pyo' -exec rm -f {} +")
    ctx.run("find . -name '*~' -exec rm -f {} +")
    ctx.run("find . -name '__pycache__' -exec rm -fr {} +")


@task
def clean_test(ctx):
    """Remove test and coverage artifacts."""
    ctx.run("rm -fr .tox/")
    ctx.run("rm -f .coverage")
    ctx.run("rm -fr htmlcov/")


@task
def clean_docs(ctx):
    """Remove docs artifacts."""
    ctx.run("make -C docs clean")


@task
def mypy(ctx):
    """Check typing with mypy."""
    ctx.run(f"{PIPENV_RUN} mypy --ignore-missing-imports {PACKAGE_NAME}")


@task(clean_build, clean_pyc, clean_test)
def clean(ctx):
    """Remove all build, test, coverage and Python artifacts."""
    ctx.run("echo clean")


@task
def lint(ctx):
    """Check style with flake8."""
    ctx.run(f"{PIPENV_RUN} flake8 {PACKAGE_NAME}")


@task
def test(ctx):
    """Run tests quickly with the default Python."""
    ctx.run(f"{PIPENV_RUN} pytest")


@task
def test_all(ctx):
    """Run tests on every Python version with tox."""
    ctx.run(f"{PIPENV_RUN} tox")


@task
def coverage(ctx):
    """Check code coverage quickly with the default Python."""
    ctx.run(f"{PIPENV_RUN} coverage run --source {PACKAGE_NAME} -m pytest")
    ctx.run(f"{PIPENV_RUN} coverage report -m")
    ctx.run(f"{PIPENV_RUN} coverage html")
    browser(path="htmlcov/index.html")


@task
def docs(ctx):
    """Generate Sphinx HTML documentation, including API docs."""
    ctx.run(f"rm -f docs/{PACKAGE_NAME}.rst")
    ctx.run(f"rm -f docs/{PACKAGE_NAME}.*.rst")
    ctx.run(f"rm -f docs/modules.rst")
    ctx.run(f"{PIPENV_RUN} make -C docs clean")
    ctx.run(f"{PIPENV_RUN} make -C docs html")
    browser(path="docs/_build/html/index.html")


@task(docs)
def servedocs(ctx):
    """Compile the docs watching for changes."""
    ctx.run(f"{PIPENV_RUN} watchmedo shell-command -p '*.rst' -c 'make -C docs html' -R -D .")


@task(clean)
def release(ctx):
    """Package and upload a release."""
    ctx.run(f"{PIPENV_RUN} python setup.py sdist upload")
    ctx.run(f"{PIPENV_RUN} python setup.py bdist_wheel upload")


@task(clean)
def dist(ctx):
    """Builds source and wheel package."""
    ctx.run(f"{PIPENV_RUN} python setup.py sdist")
    ctx.run(f"{PIPENV_RUN} python setup.py bdist_wheel")
    ctx.run(f"{PIPENV_RUN} ls -l dist")


@task
def install(ctx):
    """Installs virtual environments and requirements."""
    ctx.run("pipenv install")
    ctx.run("pipenv install --dev")
    ctx.run("pipenv lock -r > requirements.txt")
    ctx.run(f"{PIPENV_RUN} pip install -e .")
    ctx.run(
        f"""{PIPENV_RUN} python -m ipykernel install --sys-prefix --name {PACKAGE_NAME} --display-name "{PACKAGE_NAME}" """
    )


@task
def jupyter_notebook(ctx):
    """Serve the jupyter notebook."""
    ctx.run(f"{PIPENV_RUN} jupyter notebook --notebook-dir jupyter")


@task
def jupyter_lab(ctx):
    """Serve the jupyter lab."""
    ctx.run(f"{PIPENV_RUN} jupyter lab --notebook-dir jupyter")


@task
def uninstall(ctx):
    """Uninstalls virtual environments and requirements."""
    ctx.run("pipenv --rm")
