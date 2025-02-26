import re

def es_ipv4(objetivo):
    """
    Probar si es una dirección IPv4 o no
    """
    patron = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
             r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
             r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
             r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(patron, objetivo) is not None