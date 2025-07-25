import os

def is_file_exist(file_name):
    """
    Verifica si el nombre del archivo existe.  
    :param file_name: Nombre del archivo.  
    :type file_name: str  
    :return: Devuelve `True` (existe) o `False` (no existe o el nombre del archivo no es válido).  
    :rtype: bool  
    """
    if isinstance(file_name, str) and file_name:
        return os.path.isfile(file_name)
    return False