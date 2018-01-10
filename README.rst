==============
Database Tools
==============


.. image:: https://img.shields.io/travis/xguse/db_tools.svg
        :target: https://travis-ci.org/xguse/db_tools

.. image:: https://readthedocs.org/projects/db-tools/badge/?version=latest
        :target: https://db-tools.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


A set of command line executable and script importable tools to aid the Snapper Lab in managing and combining RedCap, FreezerPro, and other databases.


* Free software: MIT license
* Documentation: https://db-tools.readthedocs.io.


Features
--------

* TODO

Install for Development
-----------------------

#. Install and become familiar with `conda/Anaconda <https://conda.io/docs/user-guide/install/index.html>`_.
#. Make sure that you have (at least) the following anaconda channels activated in your ``.condarc`` file (the order is kind of important too):

        * ``anaconda``
        * ``r``
        * ``conda-forge``
        * ``bioconda``
        * ``pandas``
        * ``defaults``

#. Fork the repository to your github by clicking the "Fork" button at the top right of this project's github page.
#. Clone your forked repo to your dev computer: ``git clone git@github.com:YOUR_GITHUB_NAME/db_tools.git``.
#. Enter your freshly cloned Database Tools directory: ``cd db_tools``.
#. Run ``make help`` to see most of the ``make`` targets available.
#. Running ``make install``. This creates and registers a ``conda`` environment named db_tools. Into that conda environment, it installs all of the needed libraries to run and develop Database Tools.
#. To uninstall your dev environment just run ``make uninstall-conda-env``. All traces of the environment should be erased.
#. Remember to activate the ``conda`` env before you try to use or interact with Database Tools or you will not have access to it. That is, unless you are running a ``make`` target. In most cases, the first step of the ``make`` target will be to activate the correct env for you.

Credits
---------

This package was created with Cookiecutter_ and the `xguse/cookiecutter-pypackage`_ project template which is based on `audreyr/cookiecutter-pypackage`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`xguse/cookiecutter-pypackage`: https://github.com/xguse/cookiecutter-pypackage

