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
    data_dict = defaultdict(list)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            base_name = os.path.splitext(file_name)[0]
            if file_name.endswith('.xml'):
                with zip_ref.open(file_name) as xml_file:
                    data_dict[base_name].append(xml_file.read())
            else:
                with zip_ref.open(file_name) as other_file:
                    data_dict[base_name].append(other_file.read())
    
    return dict(data_dict)