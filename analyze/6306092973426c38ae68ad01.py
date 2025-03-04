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
        'pass': 'password'
    }