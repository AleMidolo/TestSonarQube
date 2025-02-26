import os
import sys

def is_gitbash():
    """
    Devuelve "True" si se ejecuta en un gitbash de Windows

    :return: True si es gitbash
    """
    return os.name == 'nt' and 'git' in sys.executable.lower()