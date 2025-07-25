import re

def is_ipv4(target):
    """
    测试是否为 IPv4 地址。

    返回值：布尔值，如果目标是 IPv4 地址，则返回真，否则返回假。
    """
    ipv4_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
    return bool(ipv4_pattern.match(target))