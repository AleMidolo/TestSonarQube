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
    """
    import zipfile
    from collections import defaultdict
    import os

    data_dict = defaultdict(list)

    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        for file_info in zip_file.infolist():
            if file_info.filename.endswith('.xml'):
                base_name = os.path.splitext(os.path.basename(file_info.filename))[0]
                with zip_file.open(file_info.filename) as file:
                    data_dict[base_name].append(file.read())

    return dict(data_dict)