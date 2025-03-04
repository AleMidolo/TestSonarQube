def is_local(host):
    """
    Checks if the host is the localhost

    :param host: The hostname or ip
    :return: True if the host is the localhost
    """
    localhost_names = ['localhost', '127.0.0.1', '::1', '0:0:0:0:0:0:0:1']
    return host.lower() in localhost_names