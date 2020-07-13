#!/bin/env python3
"""
    PySizer is a simple python command line program to resize images efficiently using Threads.

            https://github.com/kumaraditya303/PySizer.git

    PySizer is a command line picture resizer by Kumar Aditya.
    Copyright (c) 2020 by Kumar Aditya.

"""
import os
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor
from time import perf_counter

import click
from PIL import Image

__version__ = '1.0.0'
__author__ = 'Kumar Aditya @kumaraditya303 '

# Program start time
t1 = perf_counter()


@click.command()
@click.option('--folder', default='.', show_default=True, help='pictures folder path', type=click.Path(exists=True), required=True)
@click.option('--dest', default='resized', show_default=True, help='destination for resized pictures', type=click.Path(), required=True)
@click.option('--height', default=1920, show_default=True, help='image height in px', type=click.INT, required=True)
@click.option('--width', default=1280, show_default=True, help='image width in px', type=click.INT, required=True)
@click.option('--threads', default=50, show_default=True, help='number of threads to use', type=click.INT, required=False)
def main(folder, dest, height, width, threads):
    """
    Main PySizer function which with ThreadPoolExecutor creates threads for 
    resizing pictures.

    Checks for correct file extension, creates threads for each picture with 
    thread limitation as given by threads argument.

    Creates progress bar with the click for resizing progress.

    :param folder: the picture's folder path
    :param dest: the resized pictures destination path
    :param height: the resized picture's height
    :param width: the resized picture's width
    """
    files = [file for file in os.listdir(folder) if file.endswith(
        '.jpg') or file.endswith('.jpeg') or file.endswith('.png')]
    if len(files) == 0:
        click.secho('No pictures found!', fg='red')
        SystemExit(1)
    # Create thread pool with max_workers=threads
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = [executor.submit(resize, file, dest, height, width)
                   for file in files]
        # Creates progress bas with current resizing progress
        with click.progressbar(length=len(files), label='Picture resizing progress: ', color='green') as bar:
            for f in as_completed(results):
                bar.update(1)
        # After execution time
        t2 = perf_counter()
        click.secho(
            f'Picture resizing took {round(t2-t1,2)} seconds!', fg='green')


def resize(file, resize_folder, height, width):
    """
    Function to resize a image with PIL Library.
    """
    if not os.path.exists(resize_folder):
        os.mkdir(resize_folder)
    i = Image.open(file)
    i.thumbnail((height, width))
    i.save(f'{resize_folder}/{file}')
    return 0


# Start Program
if __name__ == '__main__':
    main()
