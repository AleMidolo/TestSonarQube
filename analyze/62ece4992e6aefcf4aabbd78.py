def is_local(host):
    """
    Verifica se l'host è il localhost.

    :param host: Il nome host o l'indirizzo IP.  
    :return: True se l'host è il localhost.
    """
    return host in ('localhost', '127.0.0.1', '::1')