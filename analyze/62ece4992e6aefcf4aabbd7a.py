import os

def is_gitbash():
    """
    Restituisce True se viene eseguito in un terminale gitbash di Windows

    :return: True se è gitbash
    """
    return 'GIT_BASH' in os.environ.get('TERM_PROGRAM', '')