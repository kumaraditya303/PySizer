#!/bin/env python
# -*- coding: utf-8 -*-
r"""
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
    for the current progress of resizing of pictures.

    Project made and maintained by Kumar Aditya
"""
import glob
import os
import time
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing import cpu_count
from typing import List, Tuple
from uuid import uuid4

import click
from PIL import Image

start_time = time.perf_counter()


@click.command()
@click.option(
    "--source",
    default=".",
    show_default=True,
    help="Source",
    type=click.Path(exists=True),
)
@click.option(
    "--dest",
    default="resized",
    show_default=True,
    help="Destination",
    type=click.Path(exists=False),
)
@click.option(
    "--height",
    default=1080,
    show_default=True,
    help="Image height",
    type=click.INT,
)
@click.option(
    "--width",
    default=1920,
    show_default=True,
    help="Image width",
    type=click.INT,
)
@click.option(
    "--threads",
    default=cpu_count() * 5,
    show_default=True,
    help="Number of threads",
    type=click.INT,
)
@click.option(
    "--recursive",
    "-r",
    default=False,
    show_default=True,
    help="Find images recursively",
    is_flag=True,
    type=click.BOOL,
)
def main(
    source: str,
    dest: str,
    height: int,
    width: int,
    threads: int,
    recursive: bool,
) -> None:
    r"""
    \b
     ____        ____  _
    |  _ \ _   _/ ___|(_)_______ _ __
    | |_) | | | \___ \| |_  / _ \ '__|
    |  __/| |_| |___) | |/ /  __/ |
    |_|    \__, |____/|_/___\___|_|
           |___/
    \b
    PySizer is a simple python command line program to resize images
    efficiently by Multi Threading and is 5 times the cpu count of the
    machine in this program and the current running threads is limited
    by the use of ThreadPoolExecutor and also displays a progress bar
    for the current progress.

    """
    os.chdir(source)
    os.makedirs(dest, exist_ok=True)
    files: List[str] = []
    if recursive:
        files.extend(glob.glob("**/*.jpg", recursive=True))
        files.extend(glob.glob("**/*.jpeg", recursive=True))
        files.extend(glob.glob("**/*.png", recursive=True))
    else:
        files.extend(glob.glob("*.jpg"))
        files.extend(glob.glob("*.jpeg"))
        files.extend(glob.glob("*.png"))

    if len(files) == 0:
        click.secho("No pictures found!", fg="red")
        os.rmdir(dest)
        return

    # Create ThreadPoolExecutor with max_workers=threads
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = [
            executor.submit(resize, file, dest, (height, width)) for file in files
        ]
        # Creates progress bar with current resizing progress
        with click.progressbar(
            length=len(files),
            label="Picture resizing progress: ",
            fill_char=click.style("█", fg="green"),
            empty_char=click.style("█", fg="bright_white"),
            show_percent=True,
        ) as bar:
            for _ in as_completed(results):
                bar.update(1)

        # After execution time
        end_time = time.perf_counter()
        click.secho(
            f"{len(files)} pictures resized in "
            f"{round(end_time-start_time,2)} seconds!",
            fg="green",
        )


def resize(file: str, dest: str, dimensions: Tuple[int, int]) -> None:
    """Function to resize a image with PIL Library."""
    i = Image.open(file)
    i.thumbnail(dimensions)
    # Create unique filename incase filename already exists
    file = os.path.split(file)[1]
    file = os.path.splitext(file)[0] + uuid4().hex[:6] + os.path.splitext(file)[1]
    with open(os.path.join(dest, file), "w") as f:
        i.save(f)
