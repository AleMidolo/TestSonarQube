def find_path_type(path):
    """
    Devuelve una cadena que indica el tipo de elemento en la ruta proporcionada.

    Valores de retorno:
        'root' - parece ser una Raíz de Almacenamiento OCFL
        'object' - parece ser un Objeto OCFL
        'file' - un archivo, podría ser un inventario
        otra cadena explica la descripción del error

    Solo examina los archivos "0=*" Namaste para determinar el tipo de directorio.
    """
    import os

    if not os.path.exists(path):
        return "La ruta no existe."

    if os.path.isdir(path):
        if any(file.startswith("0=") for file in os.listdir(path)):
            return 'root'
        else:
            return 'object'
    elif os.path.isfile(path):
        return 'file'
    else:
        return "Tipo de elemento desconocido."