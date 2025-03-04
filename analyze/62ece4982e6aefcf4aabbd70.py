def os_is_mac():
    """
    检查操作系统是否为 macOS

    :return: bool, 如果是 macOS 则返回真，否则返回假。
    :return: 如果是 macOS 则返回真
    :rtype: bool
    """
    import platform
    return platform.system().lower() == 'darwin'