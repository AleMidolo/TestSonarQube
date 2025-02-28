import platform

def os_is_mac():
    """
    Checks if the os is macOS

    :return: True if macOS
    :rtype: bool
    """
    return platform.system() == 'Darwin'