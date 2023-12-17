# -*- coding: utf-8 -*-

import sys
import subprocess
from pathlib import Path

try:
    from virtualenv_bootstrap.api import Project
except ImportError:
    _path_pip = Path(sys.executable).parent / "pip"
    subprocess.run([f"{_path_pip}", "install", "virtualenv-bootstrap"], check=True)

    from virtualenv_bootstrap.api import Project

dir_project_root = Path(__file__).absolute().parent
project = Project(dir_project_root=dir_project_root)
project.bootstrap()

# run test script
path_test_script = dir_project_root / "test_script.py"
subprocess.run([f"{project.path_venv_bin_python}", f"{path_test_script}"], check=True)

# bootstrap_py_url = "https://raw.githubusercontent.com/MacHu-GWU/virtualenv_bootstrap-project/main/bootstrap.py"
# with request.urlopen(bootstrap_py_url) as response:
#     script = response.read().decode("utf-8").strip()
#
# cwd = os.getcwd()
# os.chdir(str(dir_project_root))
# subprocess.run([sys.executable, "-c", script], check=True)
# os.chdir(cwd)

from virtualenv_bootstrap.api import Project

#
# project = Project()
# project.bootstrap()
