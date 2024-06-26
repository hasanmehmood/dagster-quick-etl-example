# from setuptools import find_packages, setup

# import pathlib

# import pkg_resources

# install_requires = []
# with pathlib.Path("requirements.txt").open() as requirements_txt:
#     install_requires = [
#         str(requirement)
#         for requirement in pkg_resources.parse_requirements(requirements_txt)
#     ]

# setup(
#     name="quickstart_etl",
#     packages=find_packages(exclude=["quickstart_etl_tests"]),
#     install_requires=install_requires,
#     extras_require={"dev": ["dagster-webserver", "pytest"]},
# )


from setuptools import find_packages, setup

setup(
    name="quickstart_etl",
    packages=find_packages(exclude=["quickstart_etl_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "boto3",
        "pandas",
        "matplotlib",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
