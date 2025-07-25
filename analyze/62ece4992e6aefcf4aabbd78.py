import socket

def is_local(host):
    """
    检查主机是否是本地主机，  
    本地主机包括本地 IP、用户名、本地域名、`localhost` 和 `127.0.0.1`。

    参数:
      host: 主机名或 IP 地址
    返回值:
      如果主机是本地主机，则返回真，否则返回假。
    检查主机是否是本地主机

    :param host: 主机名或 IP 地址
    :return: 如果主机是本地主机，则返回真，否则返回假
    """
    if host in ('localhost', '127.0.0.1'):
        return True
    
    try:
        host_ip = socket.gethostbyname(host)
        local_ips = socket.gethostbyname_ex(socket.gethostname())[2]
        if host_ip in local_ips:
            return True
    except socket.error:
        pass
    
    return False