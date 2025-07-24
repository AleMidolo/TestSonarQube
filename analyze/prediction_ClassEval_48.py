import socket


class IpUtil:

    @staticmethod
    def is_valid_ipv4(ip_address):
        return IpUtil._is_valid_ip(ip_address, socket.AF_INET)

    @staticmethod
    def is_valid_ipv6(ip_address):
        return IpUtil._is_valid_ip(ip_address, socket.AF_INET6)

    @staticmethod
    def _is_valid_ip(ip_address, family):
        try:
            socket.inet_pton(family, ip_address)
            return True
        except socket.error:
            return False

    @staticmethod
    def get_hostname(ip_address):
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
            return hostname
        except socket.herror:
            return None