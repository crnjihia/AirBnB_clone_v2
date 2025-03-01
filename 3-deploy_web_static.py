#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""

from fabric.api import *
from datetime import datetime
from os.path import exists
import os

env.hosts = ['54.164.253.166', '52.204.144.35']


def do_pack():
    """
    Generates a .tgz archive from the contents of web_static folder
    """
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")
        
        now = datetime.now()
        archive_name = "versions/web_static_{}.tgz".format(
            now.strftime("%Y%m%d%H%M%S"))
        
        local("tar -cvzf {} web_static".format(archive_name))
        
        if exists(archive_name):
            return archive_name
        return None
    except:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not exists(archive_path):
        return False

    try:
        filename = archive_path.split('/')[-1]
        no_ext = filename.split('.')[0]
        path = "/data/web_static/releases/"
        
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(filename, path, no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}{}/web_static/* {}{}/".format(path, no_ext, path, no_ext))
        run("rm -rf {}{}/web_static".format(path, no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{} /data/web_static/current".format(path, no_ext))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """
    Creates and distributes an archive to the web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
