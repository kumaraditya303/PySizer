# PySizer

![](https://img.shields.io/github/workflow/status/kumaraditya303/PySizer/CI?logo=github&style=for-the-badge) ![](https://img.shields.io/codecov/c/github/kumaraditya303/pysizer?logo=codecov&style=for-the-badge) ![](https://img.shields.io/pypi/pyversions/PySizer?logo=python&style=for-the-badge) ![](https://img.shields.io/pypi/dm/PySizer?logo=pypi&style=for-the-badge)

# Introduction

```txt
 ____        ____  _
|  _ \ _   _/ ___|(_)_______ _ __
| |_) | | | \___ \| |_  / _ \ '__|
|  __/| |_| |___) | |/ /  __/ |
|_|    \__, |____/|_/___\___|_|
       |___/
```

### PySizer is a simple python command line program to resize images efficiently by Multi Threading and is 5 times the cpu count of the machine in this program and the current running threads is limited by the use of ThreadPoolExecutor, also shows a progress bar of and also supports searching for images recursively.


# Features

- Quick & Efficient picture resizing
- Threads count is dependent on the machine i.e 5 \* cpu count
- Support to find images recursively
- Auto rename file to avoid file name clashing in recursive mode

# Quick Start

- Install the project with pip

```bash
pip install git+https://github.com/kumaraditya303/PySizer.git
Or
pip install pysizer
```

- Project will now be available as a command line utility

- Get Help

```text
$ pysizer --help
Usage: pysizer [OPTIONS]

   ____        ____  _
  |  _ \ _   _/ ___|(_)_______ _ __
  | |_) | | | \___ \| |_  / _ \ '__|
  |  __/| |_| |___) | |/ /  __/ |
  |_|    \__, |____/|_/___\___|_|
         |___/

  PySizer is a simple python command line program to resize images
  efficiently by Multi Threading and is 5 times the cpu count of the
  machine in this program and the current running threads is limited
  by the use of ThreadPoolExecutor and also displays a progress bar
  for the current progress.

Options:
  --source PATH      Source  [default: .]
  --dest PATH        Destination  [default: resized]
  --height INTEGER   Image height  [default: 1080]
  --width INTEGER    Image width  [default: 1920]
  --threads INTEGER  Number of threads  [default: 40]
  -r, --recursive    Find images recursively  [default: False]
  --help             Show this message and exit.

```

- Test the project with tox

```bash
$ tox
```

# Project Made and Maintained By Kumar Aditya
