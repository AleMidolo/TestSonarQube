def is_local(host):
    import socket

    localhost_aliases = {'localhost', '127.0.0.1'}
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        localhost_aliases.add(local_ip)
    except socket.error:
        pass

    return host in localhost_aliases