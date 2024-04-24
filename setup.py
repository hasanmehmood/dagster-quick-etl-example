from setuptools import find_packages, setup

#!/usr/bin/env python

import pathlib

import pkg_resources


with pathlib.Path("requirements.txt").open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name="quickstart_etl",
    packages=find_packages(exclude=["quickstart_etl_tests"]),
    install_requires=install_requires,
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
