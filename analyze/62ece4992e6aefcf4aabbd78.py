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
    local_hosts = {'localhost', '127.0.0.1'}
    
    try:
        # 获取主机的 IP 地址
        host_ip = socket.gethostbyname(host)
    except socket.error:
        return False
    
    # 检查是否是本地 IP 地址
    if host_ip.startswith('127.') or host_ip == '::1':
        return True
    
    # 获取本地主机名和 IP 地址
    local_hostname = socket.gethostname()
    local_ip = socket.gethostbyname(local_hostname)
    
    # 检查是否与本地主机名或 IP 地址匹配
    if host == local_hostname or host_ip == local_ip:
        return True
    
    # 检查是否在本地主机列表中
    if host in local_hosts:
        return True
    
    return False