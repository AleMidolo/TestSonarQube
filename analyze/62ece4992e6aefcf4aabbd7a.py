import os

def is_gitbash():
    """
    returns True if you run in a Windows gitbash

    :return: True if gitbash
    """
    return 'GIT_BASH' in os.environ.get('TERM_PROGRAM', '')