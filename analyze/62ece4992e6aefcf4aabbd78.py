def is_local(host):
    """
    Verifica se l'host è il localhost.
    
    :param host: Il nome host o l'indirizzo IP.
    :return: True se l'host è il localhost.
    """
    localhost_names = ['localhost', '127.0.0.1', '::1', '0:0:0:0:0:0:0:1']
    return host.lower() in localhost_names