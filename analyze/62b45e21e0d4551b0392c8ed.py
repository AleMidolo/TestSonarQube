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
        # Check for "0=*" files in the directory
        for item in os.listdir(path):
            if item.startswith("0="):
                if item == "0=inventory":
                    return "file"
                else:
                    return "object"
        return "root"
    
    return "La ruta no es un directorio."