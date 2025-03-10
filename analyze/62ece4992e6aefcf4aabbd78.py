def is_local(host):
    """
    Checks if the host is the localhost

    :param host: The hostname or ip
    :return: True if the host is the localhost
    """
    local_hosts = ['localhost', '127.0.0.1', '::1']
    return host in local_hosts