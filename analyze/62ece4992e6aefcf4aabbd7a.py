def is_gitbash():
    """
    यदि आप Windows के Gitbash में प्रोग्राम चला रहे हैं तो True रिटर्न करता है।

    :return: यदि Gitbash है तो True
    """
    import os
    import sys
    
    # Check if running on Windows
    if sys.platform != 'win32':
        return False
        
    # Check for MINGW in environment variables which indicates GitBash
    if 'MINGW' in os.environ.get('MSYSTEM', ''):
        return True
        
    # Check for common GitBash paths in PATH variable
    path = os.environ.get('PATH', '').lower()
    if 'git\\mingw' in path or 'git\\usr\\bin' in path:
        return True
        
    return False