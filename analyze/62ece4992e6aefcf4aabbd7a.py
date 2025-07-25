import os

def is_gitbash():
    """
    Devuelve "True" si se ejecuta en un gitbash de Windows

    :return: True si es gitbash
    """
    return 'GITBASH' in os.environ.get('TERM_PROGRAM', '').upper()