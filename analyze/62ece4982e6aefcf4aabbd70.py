import platform

def os_is_mac():
    """
    Verifica se il sistema operativo è macOS

    :return: True se il sistema operativo è macOS
    :rtype: bool
    """
    return platform.system() == "Darwin"