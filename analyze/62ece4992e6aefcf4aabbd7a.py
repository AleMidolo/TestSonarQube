def is_gitbash():
    """
    Devuelve "True" si se ejecuta en un gitbash de Windows

    :return: True si es gitbash
    """
    import os
    import platform

    # Check if running on Windows
    if platform.system() != 'Windows':
        return False

    # Check for MINGW in environment variables which indicates Git Bash
    if 'MINGW' in os.environ.get('MSYSTEM', ''):
        return True

    return False