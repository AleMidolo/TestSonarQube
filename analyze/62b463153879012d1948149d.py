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
        Diccionario donde las claves son los nombres base de los archivos XML y los valores son listas de archivos asociados.
    """
    file_groups = defaultdict(list)
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.xml'):
                base_name = os.path.splitext(file)[0]
                file_groups[base_name].append(os.path.join(root, file))
    
    return dict(file_groups)