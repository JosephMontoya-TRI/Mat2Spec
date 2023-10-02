#!/usr/bin/env python
from setuptools import find_packages, setup

# setup_requires = []
# 
# install_requires = [
#     "atomate==1.1.0"
# ]


setup(
    name="mat2spec",
    version="0.1",
    description="Mat2Spec",
    author="TMC-CRM",
    packages=find_packages(),
    # If any non-python files are required for distribution,
    # e.g. YAML or the like, they should go here
    # package_data={"": ["**/*.jar"]},
    # setup_requires=setup_requires,
    # install_requires=install_requires,
    include_package_data=True,
    python_requires=">=3.6, <4",
)
