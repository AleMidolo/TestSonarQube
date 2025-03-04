def is_gitbash():
    """
    Restituisce True se viene eseguito in un terminale gitbash di Windows

    :return: True se è gitbash
    """
    import os
    import sys
    
    # Check if running on Windows
    if sys.platform != 'win32':
        return False
        
    # Check for MINGW in environment variables which indicates GitBash
    if 'MINGW' in os.environ.get('MSYSTEM', ''):
        return True
        
    return False