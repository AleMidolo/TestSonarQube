def is_local(host):
    """
    Verifica si el host es el localhost.

    :param host: El nombre del host o la dirección IP.
    :return: True si el host es el localhost, de lo contrario False.
    """
    localhost_names = {'localhost', '127.0.0.1', '::1'}
    return host in localhost_names