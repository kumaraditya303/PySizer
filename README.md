# PySizer

![](https://travis-ci.com/kumaraditya303/PySizer.svg?token=Tp128txvcHsePdipY3xq&branch=master) ![](https://img.shields.io/codecov/c/github/kumaraditya303/PySizer?style=flat-square) ![](https://img.shields.io/pypi/pyversions/PySizer?style=flat-square) ![](https://img.shields.io/pypi/dm/PySizer)

# Introduction

### PySizer is a simple python command line program to resize images efficiently by Multi Threading and is 5 times the cpu count of the machine in this program and the current running threads is limited by the use of ThreadPoolExecutor and also displays a progress bar for the current progress.

# Quick Start

- Install the project with pip

```bash
pip install git+https://github.com/kumaraditya303/PySizer.git
```

- Project will now be available as a command line utility

- Get Help

```text
$ pysizer.exe --help
Usage: pysizer [OPTIONS]

  PySizer is a simple python command line program to resize images
  efficiently by Multi Threading and is 5 times the cpu count of the machine
  in this program and the current running threads is limited by the use of
  ThreadPoolExecutor and also displays a progress bar for the current
  progress.

Options:
  --source PATH      Source  [default: .]
  --dest PATH        Destination  [default: resized]
  --height INTEGER   Image height  [default: 1080]
  --width INTEGER    Image width  [default: 1920]
  --threads INTEGER  Number of threads  [default: 40]
  --help             Show this message and exit.
```

- Test the project with tox

```sh
$ tox
```

# Project Made and Maintained By Kumar Aditya
