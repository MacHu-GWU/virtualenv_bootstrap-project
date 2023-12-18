# -*- coding: utf-8 -*-

import sys
import subprocess
from urllib import request
from pathlib import Path

dir_project_root = Path(__file__).absolute().parent
path_requirements_txt = dir_project_root / "requirements.txt"


def get_url_content(url) -> str:
    with request.urlopen(url) as response:
        return response.read().decode("utf-8").strip()


bootstrap_py_url = "https://raw.githubusercontent.com/MacHu-GWU/virtualenv_bootstrap-project/main/bootstrap.py"
script = get_url_content(bootstrap_py_url)
args = [
    sys.executable,
    "-c",
    script,
    "--dir_project_root",
    f"{dir_project_root}",
    "--python_version",
    f"{sys.version_info.major}.{sys.version_info.minor}",
    "--path_requirements_txt_or_pyproject_toml",
    f"{path_requirements_txt}",
]
subprocess.run(args, check=True)


# run test script
path_venv_bin_python = dir_project_root / ".venv" / "bin" / "python"
path_test_script = dir_project_root / "test_script.py"
subprocess.run([f"{path_venv_bin_python}", f"{path_test_script}"], check=True)
