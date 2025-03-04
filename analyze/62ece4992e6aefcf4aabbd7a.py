def is_gitbash():
    """
    यदि आप Windows के Gitbash में प्रोग्राम चला रहे हैं तो True रिटर्न करता है।

    :return: यदि Gitbash है तो True
    """
    import os
    import sys
    
    # Check if running on Windows
    if os.name != 'nt':
        return False
        
    # Check for MINGW in system path which indicates GitBash
    if 'MINGW' in sys.executable.upper():
        return True
        
    # Check for common GitBash environment variables
    if os.environ.get('MSYSTEM', '').startswith('MINGW'):
        return True
        
    return False