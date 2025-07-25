import os
from collections import defaultdict

def _explore_folder(folder):
    """
    Obtiene los datos de los paquetes desde la carpeta.

    Agrupa los archivos por el nombre base de su archivo XML y devuelve los datos en formato de diccionario.

    Parámetros
    ----------
    folder : str
        Carpeta del paquete

    Retorna
    -------
    dict
        Diccionario con los archivos agrupados por el nombre base del archivo XML.
    """
    file_groups = defaultdict(list)
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.xml'):
                base_name = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)
                file_groups[base_name].append(file_path)
    
    return dict(file_groups)