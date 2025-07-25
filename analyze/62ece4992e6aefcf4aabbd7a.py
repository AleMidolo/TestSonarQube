def is_gitbash():
    """
    returns True if you run in a Windows gitbash

    :return: True if gitbash
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