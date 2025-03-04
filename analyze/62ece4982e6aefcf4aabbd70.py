def os_is_mac():
    """
    Verifica si el sistema operativo es macOS

    :return: True si es macOS
    :rtype: bool
    """
    import platform
    return platform.system().lower() == 'darwin'