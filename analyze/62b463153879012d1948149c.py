import os

def select_filenames_by_prefix(prefix, files):
    """
    Obtén los archivos que pertenecen a un paquete de documentos.

    Retorna los archivos de la lista `files` cuyos nombres comienzan con `prefix`.

    Parámetros
    ----------
    prefix : str  
    Prefijo del nombre del archivo.  

    files : lista de str  
    Rutas de los archivos.  

    Retorna
    -------
    list  
    Lista de rutas de archivos cuyos nombres base coinciden con el prefijo `prefix`.
    """
    selected_files = []
    for file_path in files:
        file_name = os.path.basename(file_path)
        if file_name.startswith(prefix):
            selected_files.append(file_path)
    return selected_files