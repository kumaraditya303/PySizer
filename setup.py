#!/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="PySizer",
    author="Kumar Aditya",
    author_email="",
    description="Quick & Efficient Command Line picture resizer!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="Pillow ThreadPoolExecutor",
    url="https://github.com/kumaraditya303/PySizer",
    packages=["pysizer"],
    include_package_data=True,
    install_requires=["Pillow>=8.0.1,<9.0.0", "click>=7.1.2,<8.0.0"],
    entry_points={"console_scripts": ["pysizer=pysizer:main"]},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
    use_scm_version=True,
    python_requires=">=3.7",
    setup_requires=["setuptools_scm", "wheel"],
)
