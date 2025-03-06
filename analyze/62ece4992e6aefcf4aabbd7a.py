def is_gitbash():
    """
    Restituisce True se viene eseguito in un terminale gitbash di Windows

    :return: True se è gitbash
    """
    import os
    return os.environ.get('TERM_PROGRAM') == 'mintty' and os.environ.get('SHELL') and 'bash' in os.environ.get('SHELL')