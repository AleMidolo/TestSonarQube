import os
import platform

def is_gitbash():
    """
    Restituisce True se viene eseguito in un terminale gitbash di Windows

    :return: True se è gitbash
    """
    return platform.system() == "Windows" and "gitbash" in os.environ.get("TERM", "").lower()