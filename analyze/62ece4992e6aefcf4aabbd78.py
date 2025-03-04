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
    import socket
    
    # 转换为小写进行比较
    host = host.lower()
    
    # 检查是否为localhost或127.0.0.1
    if host in ['localhost', '127.0.0.1']:
        return True
        
    # 获取本机主机名
    local_hostname = socket.gethostname().lower()
    if host == local_hostname:
        return True
        
    # 获取本机IP地址
    try:
        local_ip = socket.gethostbyname(local_hostname)
        if host == local_ip:
            return True
    except socket.gaierror:
        pass
        
    # 获取本机所有IP地址
    try:
        local_ips = [ip for ip in socket.gethostbyname_ex(local_hostname)[2]]
        if host in local_ips:
            return True
    except socket.gaierror:
        pass
        
    return False