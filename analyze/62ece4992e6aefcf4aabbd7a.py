import os

def is_gitbash():
    """
    Devuelve "True" si se ejecuta en un gitbash de Windows

    :return: True si es gitbash
    """
    return 'GIT_BASH' in os.environ.get('TERM_PROGRAM', '')