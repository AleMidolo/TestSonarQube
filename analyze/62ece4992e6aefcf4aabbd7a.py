import os
import platform

def is_gitbash():
    return platform.system() == "Windows" and "git" in os.environ.get("SHELL", "")