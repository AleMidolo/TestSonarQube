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
    import os
    from collections import defaultdict
    
    # Diccionario para almacenar los archivos agrupados
    grouped_files = defaultdict(list)
    
    # Abrir el archivo zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Iterar sobre todos los archivos en el zip
        for filename in zip_ref.namelist():
            # Obtener el nombre base del archivo (sin extensión)
            base_name = os.path.splitext(os.path.basename(filename))[0]
            
            # Si el archivo es XML, usarlo como clave para agrupar
            if filename.lower().endswith('.xml'):
                base_key = base_name
                # Agregar todos los archivos que comparten el mismo nombre base
                for related_file in zip_ref.namelist():
                    related_base = os.path.splitext(os.path.basename(related_file))[0]
                    if related_base == base_name:
                        grouped_files[base_key].append(related_file)
    
    # Convertir defaultdict a dict regular
    return dict(grouped_files)