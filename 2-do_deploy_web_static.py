#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import local, put, run, env, sudo
from datetime import datetime
from os import path

env.hosts = ['100.25.103.21', '34.205.65.150']


def do_deploy(archive_path):
    """Function to deploy"""
    if not path.exists(archive_path):
        return False
    try:
        # Upload archive to /tmp/ directory on web servers
        put(archive_path, "/tmp/")

        # Extract archive to /data/web_static/releases/<filename> directory
        filename = archive_path.split('/')[-1]  # Extract filename from path
        name = filename.split('.')[0]  # Extract filename without extension
        release_path = "/data/web_static/releases/{}/".format(name)
        sudo("mkdir -p {}".format(release_path))
        sudo("tar -xzf /tmp/{} -C {}".format(filename, release_path))

        # Remove archive from /tmp/ directory
        run("rm /tmp/{}".format(filename))

        # Move contents of extracted folder to release_path
        sudo("mv {}web_static/* {}".format(release_path, release_path))

        # Clean up extracted folder
        sudo("rm -rf {}web_static".format(release_path))

        # Update symbolic link
        current_path = "/data/web_static/current"
        sudo("rm -rf {}".format(current_path))
        sudo("ln -s {} {}".format(release_path, current_path))

        return True
    except Exception as e:
        print("Exception:", e)
        return False
