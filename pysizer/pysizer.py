#!/bin/env python
"""
    PySizer is a simple python command line program to resize images 
    efficiently by Multi Threading and is 5 times the cpu count of the 
    machine in this program and the current running threads is limited
    by the use of ThreadPoolExecutor and also displays a progress bar 
    for the current progress of resizing of pictures.

    Install with 
    - pip install git+https://github.com/kumaraditya303/PySizer.git

    Project made and maintained by Kumar Aditya 
"""
import os
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing import cpu_count
from time import perf_counter

import click
from PIL import Image

start_time = perf_counter()


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
def main(source: str, dest: str, height: int, width: int, threads: int) -> None:
    """
    PySizer is a simple python command line program to resize images
    efficiently by Multi Threading and is 5 times the cpu count of the
    machine in this program and the current running threads is limited
    by the use of ThreadPoolExecutor and also displays a progress bar
    for the current progress.
    """

    if not os.path.exists(dest):
        os.mkdir(dest)
    files = [
        file for file in os.listdir(source) if file.endswith((".jpg", ".jpeg", ".png"))
    ]
    if len(files) == 0:
        click.secho("No pictures found!", fg="red")
        exit()

    # Create thread pool executor with max_workers=threads
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = [executor.submit(resize, file, dest, height, width) for file in files]
        # Creates progress bar with current resizing progress
        with click.progressbar(
            length=len(files), label="Picture resizing progress: ", color="green"
        ) as bar:
            for _ in as_completed(results):
                bar.update(1)

        # After execution time
        end_time = perf_counter()
        click.secho(
            f"Picture resizing took {round(end_time-start_time,2)} seconds!", fg="green"
        )


def resize(file: str, dest: str, height: int, width: int) -> None:
    """Function to resize a image with PIL Library."""
    i = Image.open(file)
    i.thumbnail((height, width))
    i.save(os.path.join(dest, file))
