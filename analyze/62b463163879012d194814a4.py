import zipfile
import os
from collections import defaultdict

def _explore_zipfile(zip_path):
    """
    Obtiene los datos de los paquetes desde `zip_path`.

    Agrupa los archivos por el nombre base de su archivo XML y devuelve los datos en formato de diccionario.

    Parámetros
    ----------
    zip_path: str  
        Ruta del archivo zip.
    Retorna
    -------
    dict  
        Diccionario que agrupa los archivos por el nombre base de su archivo XML.
    """
    data = defaultdict(list)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            base_name = os.path.splitext(file_name)[0]
            if base_name.endswith('.xml'):
                base_name = base_name[:-4]  # Remove '.xml' from the base name
            with zip_ref.open(file_name) as file:
                data[base_name].append(file.read())
    
    return dict(data)