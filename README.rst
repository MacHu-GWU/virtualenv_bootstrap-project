
.. image:: https://readthedocs.org/projects/virtualenv-bootstrap/badge/?version=latest
    :target: https://virtualenv-bootstrap.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/virtualenv_bootstrap-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/virtualenv_bootstrap-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/virtualenv_bootstrap-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/virtualenv_bootstrap-project

.. image:: https://img.shields.io/pypi/v/virtualenv-bootstrap.svg
    :target: https://pypi.python.org/pypi/virtualenv-bootstrap

.. image:: https://img.shields.io/pypi/l/virtualenv-bootstrap.svg
    :target: https://pypi.python.org/pypi/virtualenv-bootstrap

.. image:: https://img.shields.io/pypi/pyversions/virtualenv-bootstrap.svg
    :target: https://pypi.python.org/pypi/virtualenv-bootstrap

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/virtualenv_bootstrap-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/virtualenv_bootstrap-project

------

.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://virtualenv-bootstrap.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://virtualenv-bootstrap.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/virtualenv_bootstrap-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/virtualenv_bootstrap-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/virtualenv_bootstrap-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/virtualenv-bootstrap#files


Welcome to ``virtualenv_bootstrap`` Documentation
==============================================================================
在自动化运维领域, 用 Python 来代替 Bash 来写 shell script 能够极大的提升代码的可维护性. 仅使用标准库就能做到大部分的事情了. 在少数情况下, 我们依然需要安装一些第三方库来完成一些业务逻辑. 通常情况下, 我们需要手动安装依赖, 还有可能需要用到 virtualenv 以避免污染 global Python, 然后才能运行脚本. 这个库的意义是简化这一步骤, 通过自动创建 virtualenv 和安装依赖的方式, 使得你用任何 Python 解释器都能运行你的 shell script.


.. _install:

Install
------------------------------------------------------------------------------

``virtualenv_bootstrap`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install virtualenv-bootstrap

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade virtualenv-bootstrap
