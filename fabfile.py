#!/usr/bin/python3
from fabric import task
from fabric import Connection
import os
from datetime import datetime
from os.path import exists

# Import the functions from your deployment script
from three_deploy_web_static import do_pack, do_deploy, deploy

@task
def pack(c):
    """Create a tar gzipped archive."""
    return do_pack()

@task
def deploy_archive(c, archive_path):
    """Deploy archive to web servers."""
    return do_deploy(archive_path)

@task
def full_deploy(c):
    """Full deployment."""
    return deploy()
