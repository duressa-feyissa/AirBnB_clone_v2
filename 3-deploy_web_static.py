#!/usr/bin/python3
"""
    Fabric
"""
from fabric.api import *
from datetime import datetime
from os.path import isdir
env.hosts = ["52.91.125.60", "54.162.77.132"]


def do_pack():
    """
        genereate a trz archive
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fileName = "versions/web_static_{}".format(date)
        local("tar -cvzf {} abc".format(fileName))
        return fileName
    except:
        return None

def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

def do_deploy(archive_path):
    """
    Using the new path of the new archive
    """
    if archive_path is None:
        return False
    try:
        fileNo = archive_path.split('/').[-1]
        no_ext = fileNo.split(".")[0]
        path = "/data/web_static/releases/"
        sybol_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(fileNo, path, no_ext))
        run("rm /tmp/{}".format(fileNo))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, fileNo))
        run("rm -rf {}/web_static".format(path))
        run("rm -rf {}".format(sybol_link))
        run("ln -s {} {}".format(path, sybol_link))
        return True
    except Exception as e:
        return False
 
