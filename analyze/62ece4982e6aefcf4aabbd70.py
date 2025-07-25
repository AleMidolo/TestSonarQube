import platform

def os_is_mac():
    """
    Verifica si el sistema operativo es macOS

    :return: True si es macOS
    :rtype: bool
    """
    return platform.system() == 'Darwin'