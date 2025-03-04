def match(filename):
    """
    Verificar si el nombre de archivo es un tipo que este módulo soporta

    Argumentos:
        filename: Nombre de archivo a verificar
    Retorna:
        'False' si no es compatible, 'True' si es soportado
    """
    # Lista de extensiones soportadas
    supported_extensions = ['.txt', '.doc', '.docx', '.pdf', '.rtf']
    
    # Obtener la extensión del archivo en minúsculas
    file_extension = filename.lower().split('.')[-1]
    if not file_extension:
        return False
        
    # Verificar si la extensión está en la lista de soportadas
    return f'.{file_extension}' in supported_extensions