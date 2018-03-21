*******
History
*******

v0.1.0 / 2018-03-21
===================

  * etl.redcap: restructured for RedCapColumnInfo
  * etl.redcap: class RedCapColumnInfo
  * etl.redcap: digest_ddict
  * etl.redcap: updated ccs_labels_to_mapper
  * etl.redcap.loaders: load_data_dict
  * etl.common.recode: to_hour_minute
  * etl.common.validate: isalpha, istime
  * Makefile switched from conda to pipenv
  * switch to Pipfile for reqs
  * added initial testing suite focus: factories
  * changed column factories to use `None` not NaN for missing
  * removed useless boilerplate tests
  * added `errors.py`
  * changed call signature of etl.redcap.yesno_column_factory
  * support import form: `from db_tools.etl import common`
  * added Michael's redcap validators
  * added etl.redcap.columns to support multiple sources
  * moved Michael's columns to `sandbox`
  * Finish pull-from-mike
  * ignore annoying files like `.DS_Store`
  * Merge branch 'develop-mlesfield' into feature/pull-from-mike
  * changed gitignore logic in data/
  * -validate.py: float and date validators -__init__.py: get_failed_values function for recoding assistance -loaders.py: load columns for some floats and dates
  * etl.redcap: added Column factories for checkbox, radio, dropdown, yesno
  * etl: added is_subset
  * etl.common.recode: added nan_to_none, to_str, to_one_or_zero, setify_drop_nones
  * Filled out etl pkg structure
  * don't lint tests/ for now
  * setup.cfg ignore pylint: C0304
  * setup.cfg ignore flake8: W292
  * setup.py: fixed find_packages()
  * Added data dir with ignore instructions
  * clean up main .gitignore
  * Merge branch 'master' into develop
  * table_enforcer set to install from pypi
  * update table_enforcer version req
  * Merge remote-tracking branch 'upstream/develop' into develop
  * PULL_REQUEST_TEMPLATE.md: simplified
  * README: updated badges and dev install
  * Added `etl` subpackage
  * added template jupyter notebook
  * reqs.jupyter: remove jupyter_nbextensions_configurator
  * Makefile: uninstall-conda-env > uninstall

v0.0.4 / 2018-01-26
===================

  * update table_enforcer version req
  * PULL_REQUEST_TEMPLATE.md: simplified
  * README: updated badges and dev install
  * Added `etl` subpackage
  * added template jupyter notebook
  * reqs.jupyter: remove jupyter_nbextensions_configurator
  * Makefile: uninstall-conda-env > uninstall
  * Merge pull request #1 from xguse/feature/read_redcap
  * finished read_redcap.
  * added very useful functions
  * changelog(v0.0.3)
  * Makefile: changed --notebook-dir to jupyter
  * README: Fixed fork link

v0.0.3 / 2018-01-09
===================

  * Makefile: changed --notebook-dir to jupyter
  * README: Fixed fork link

v0.0.2 / 2018-01-09
===================

  * README: fixed urls in dev install docs

v0.0.1 / 2018-01-09
===================


* First commit