import os
import subprocess

# from
# https://stackoverflow.com/questions/281888/open-explorer-on-a-file
from os.path import join

FILE_BROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')


def explore():
    directory = os.path.expanduser("~")
    if not os.path.isdir(join(directory, "MusicCharts")):
        os.mkdir(join(directory, "MusicCharts"))
    directory = join(directory, "MusicCharts")

    if os.path.isdir(directory):
        subprocess.run([FILE_BROWSER_PATH, directory])
    elif os.path.isfile(directory):
        subprocess.run([FILE_BROWSER_PATH, '/select,', os.path.normpath(directory)])
