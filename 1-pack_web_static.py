#!/usr/bin/env bash
"""
    Fabric
"""
from fabric.api import *
from datetime import datetime
from os.path import isdir


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

