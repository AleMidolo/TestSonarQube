def os_is_mac():
    """
    जाँच करता है कि ऑपरेटिंग सिस्टम macOS है या नहीं।

    :return: यदि macOS है तो True
    :rtype: bool
    """
    import platform
    return platform.system() == "Darwin"