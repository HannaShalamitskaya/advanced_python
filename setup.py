import os
from setuptools import setup


def read(file_name):
    try:
        with open(os.path.join(os.path.dirname(__file__), file_name)) as fr:
            file_data = fr.read()
    except (FileNotFoundError, IOError):
        file_data = ""
    return file_data


setup(
    name='knapsack_problem',
    version='1.0',
    description="Examples of using greedy algorithm for solving knapsack "
                "problem",
    author='Hanna_Shalamitskaya',
    author_email='Hanna_Shalamitskaya@epam.com',
    url="https://github.com/HannaShalamitskaya",
    scripts=["start_app.py"],
    packages=['knapsack_problem'],
    package_data={'knapsack_problem': ['data/*.csv']},
    long_description=read("README")
)
