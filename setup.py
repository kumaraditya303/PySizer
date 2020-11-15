#!/bin/env python
from setuptools import find_packages, setup

setup(
    name="PySizer",
    version="0.1.2",
    author="Kumar Aditya",
    author_email="",
    description="Quick & Efficient Command Line picture resizer!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="Pillow ThreadPoolExecutor",
    url="https://github.com/kumaraditya303/PySizer",
    packages=find_packages(exclude=["tests"]),
    install_requires=["Pillow>=8.0.1,<9.0.0", "click>=7.1.2,<8.0.0"],
    entry_points={"console_scripts": ["pysizer=pysizer:main"]},
    classifiers=["Topic :: Utilities"],
    setup_requires=["setuptools", "wheel"],
    python_requires=">=3.6",
)
