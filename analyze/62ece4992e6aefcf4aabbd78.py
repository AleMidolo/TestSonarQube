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
    # 本地主机名和IP地址列表
    local_hosts = {'localhost', '127.0.0.1'}
    
    # 获取本地主机名
    local_hostname = socket.gethostname()
    local_hosts.add(local_hostname)
    
    # 获取本地IP地址
    local_ip = socket.gethostbyname(local_hostname)
    local_hosts.add(local_ip)
    
    # 获取本地域名
    try:
        local_fqdn = socket.getfqdn()
        local_hosts.add(local_fqdn)
    except:
        pass
    
    # 检查主机是否是本地主机
    return host in local_hosts