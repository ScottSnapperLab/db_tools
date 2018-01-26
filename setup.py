#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import setup, find_packages
import inspect
from pathlib import Path

HOME_DIR = Path(inspect.getfile(inspect.currentframe())).parent


def filter_req_paths(paths, func):
    """Return list of filtered libs."""
    if not isinstance(paths, list):
        raise ValueError("Paths must be a list of paths.")

    libs = set()
    junk = set(['\n'])
    for p in paths:
        with p.open(mode='r') as reqs:
            lines = set([line for line in reqs if func(line)])
            libs.update(lines)

    return list(libs - junk)


def is_pipable(line):
    """Filter for pipable reqs."""
    if "# not_pipable" in line:
        return False
    elif line.startswith('#'):
        return False
    else:
        return True


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = filter_req_paths(
    paths=[HOME_DIR / "requirements.txt", HOME_DIR / "requirements.pip.txt"], func=is_pipable
)

setup_requirements = ["pytest-runner"]

test_requirements = test_requirements = ["pytest"]

setup(
    name='db_tools',
    version='0.0.4',
    description=
    "A set of command line executable and script importable tools to aid the Snapper Lab in managing and combining RedCap, FreezerPro, and other databases.",
    long_description=readme + '\n\n' + history,
    author="Gus Dunn",
    author_email='w.gus.dunn@gmail.com',
    url='https://github.com/xguse/db_tools',
    packages=find_packages(include=['db_tools']),
    entry_points={'console_scripts': ['db_tools=db_tools.cli:main']},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='db_tools',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
