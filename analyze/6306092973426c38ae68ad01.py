def get_deprecated_args(self):
    """
    Devolviendo un diccionario con opciones que deprecian a otras.
    """
    return {
        'username': 'user',
        'passwd': 'password',
        'hostname': 'host',
        'dbname': 'database',
        'db': 'database',
        'timeout': 'connect_timeout',
        'sslmode': 'ssl_mode',
        'sslcert': 'ssl_cert',
        'sslkey': 'ssl_key',
        'sslrootcert': 'ssl_ca',
        'ssl': 'ssl_enable',
        'client_encoding': 'encoding'
    }