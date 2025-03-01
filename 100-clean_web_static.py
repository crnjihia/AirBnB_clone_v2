#!/usr/bin/python3
"""
Deletes out-of-date archives.
Usage: fab -f 100-clean_web_static.py do_clean:number=2
       -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

# Define the hosts where the script will run
env.hosts = ['54.164.253.166', '52.204.144.35']


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.
        If number is 0 or 1, keeps only the most recent archive.
        If number is 2, keeps the most and second-most recent archives,
        and so on.
    """
    # Ensure that we keep at least one archive
    number = 1 if int(number) == 0 else int(number)

    # List and sort the archives in the 'versions' directory
    archives = sorted(os.listdir("versions"))

    # Remove older archives, keeping the specified number
    [archives.pop() for i in range(number)]  # Remove the last 'number' archives
    with lcd("versions"):
        # Remove the outdated archives from the local 'versions' directory
        [local("rm ./{}".format(a)) for a in archives]

    # Change to the remote directory where releases are stored
    with cd("/data/web_static/releases"):
        # List and sort the archives in the remote directory
        archives = run("ls -tr").split()
        # Filter to include only archives that contain 'web_static_'
        archives = [a for a in archives if "web_static_" in a]

        # Remove older remote archives, keeping the specified number
        [archives.pop() for i in range(number)]  # Remove the last 'number' archives
        # Remove the outdated archives from the remote server
        [run("rm -rf ./{}".format(a)) for a in archives]
