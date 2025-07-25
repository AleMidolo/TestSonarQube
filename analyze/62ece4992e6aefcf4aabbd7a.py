def is_gitbash():
    """
    returns True if you run in a Windows gitbash

    :return: True if gitbash
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