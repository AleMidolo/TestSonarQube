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
            
            # Si el archivo termina en .xml
            if filename.lower().endswith('.xml'):
                # Usar el nombre base como clave
                key = base_name
            else:
                # Para otros archivos, buscar el nombre base del XML relacionado
                # Asumiendo que los archivos relacionados comparten el mismo nombre base
                key = base_name.split('_')[0]  # Ajustar según el patrón de nombres
            
            # Agregar el archivo al grupo correspondiente
            grouped_files[key].append(filename)
    
    # Convertir defaultdict a dict regular
    return dict(grouped_files)