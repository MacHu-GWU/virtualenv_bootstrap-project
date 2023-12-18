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
