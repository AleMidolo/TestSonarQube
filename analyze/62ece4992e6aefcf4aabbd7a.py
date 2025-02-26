import os
import platform

def is_gitbash():
    """
    returns True if you run in a Windows gitbash

    :return: True if gitbash
    """
    return platform.system() == "Windows" and "git-bash" in os.environ.get("TERM", "")