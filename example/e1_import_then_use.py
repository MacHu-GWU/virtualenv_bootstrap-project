# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path
from virtualenv_bootstrap.api import Project

dir_project_root = Path(__file__).absolute().parent

project = Project(dir_project_root=dir_project_root)
project.bootstrap()

path_test_script = dir_project_root / "test_script.py"
subprocess.run([f"{project.path_venv_bin_python}", f"{path_test_script}"])
