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
    grouped_files = defaultdict(list)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            base_name = os.path.basename(file_name)
            if base_name.endswith('.xml'):
                base_name_without_ext = os.path.splitext(base_name)[0]
                grouped_files[base_name_without_ext].append(file_name)
    
    return dict(grouped_files)