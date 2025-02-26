def match(filename):
    """
    Verificar si el nombre de archivo es un tipo que este módulo soporta

    Argumentos:
        filename: Nombre de archivo a verificar
    Retorna:
        'False' si no es compatible, 'True' si es soportado
    """
    supported_extensions = ['.txt', '.csv', '.json', '.xml']  # Ejemplo de extensiones soportadas
    return any(filename.endswith(ext) for ext in supported_extensions)