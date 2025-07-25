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
        
    # Check for MINGW in environment variables which indicates Git Bash
    if 'MINGW' in os.environ.get('MSYSTEM', ''):
        return True
        
    # Check for Git Bash specific environment variables
    if os.environ.get('TERM') == 'xterm' and os.environ.get('SHELL', '').endswith('bash.exe'):
        return True
        
    return False