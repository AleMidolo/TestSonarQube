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
    # 本地主机名
    local_hostnames = {'localhost', '127.0.0.1'}
    
    # 获取本地主机名
    local_hostname = socket.gethostname()
    
    # 获取本地 IP 地址
    local_ip = socket.gethostbyname(local_hostname)
    
    # 检查主机是否是本地主机名或 IP
    if host in local_hostnames or host == local_hostname or host == local_ip:
        return True
    
    # 检查主机是否是本地域名的别名
    try:
        host_ip = socket.gethostbyname(host)
        if host_ip == local_ip:
            return True
    except socket.error:
        pass
    
    return False