# -*- coding: utf-8 -*-

import sys
import argparse
import subprocess
from pathlib import Path


def main(
    dir_project_root: Path,
    python_version: str,
    path_requirements_txt_or_pyproject_toml: Path,
):
    try:
        from virtualenv_bootstrap.api import Project
    except ImportError:
        _path_pip = Path(sys.executable).parent / "pip"
        subprocess.run([f"{_path_pip}", "install", "virtualenv-bootstrap"], check=True)

        from virtualenv_bootstrap.api import Project

    project = Project(
        dir_project_root=dir_project_root,
        python_version=python_version,
        path_requirements_txt_or_pyproject_toml=path_requirements_txt_or_pyproject_toml,
    )
    project.bootstrap(recreate_venv=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir_project_root", required=True)
    parser.add_argument("--python_version", required=True)
    parser.add_argument("--path_requirements_txt_or_pyproject_toml", required=True)

    args = parser.parse_args()
    # fmt: off
    main(
        dir_project_root=Path(args.dir_project_root),
        python_version=args.python_version,
        path_requirements_txt_or_pyproject_toml=Path(args.path_requirements_txt_or_pyproject_toml),
    )
    # fmt: on
