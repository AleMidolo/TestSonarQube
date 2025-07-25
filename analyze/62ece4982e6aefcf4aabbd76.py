def match(filename):
    """
    Verificar si el nombre de archivo es un tipo que este módulo soporta

    Argumentos:
        filename: Nombre de archivo a verificar
    Retorna:
        'False' si no es compatible, 'True' si es soportado
    """
    # Lista de extensiones soportadas
    supported_extensions = ['.txt', '.csv', '.json', '.xml']
    
    # Verificar si el archivo tiene una extensión soportada
    return any(filename.endswith(ext) for ext in supported_extensions)