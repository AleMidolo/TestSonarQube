import os
import platform

def is_gitbash():
    """
    Devuelve "True" si se ejecuta en un gitbash de Windows

    :return: True si es gitbash
    """
    return platform.system() == "Windows" and "git" in os.environ.get("SHELL", "")