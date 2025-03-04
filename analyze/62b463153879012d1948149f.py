def _eval_file(prefix, file_path):
    """
    Identifica el tipo de archivo del paquete: `asset` o `rendition`.

    Identifica el tipo de archivo del paquete y actualiza `packages` con el tipo y
    la ruta del archivo en análisis.

    Parámetros
    ----------
    prefix : str
        nombre del archivo XML sin extensión
    filename : str
        nombre del archivo
    file_folder : str
        carpeta del archivo

    Retorna
    -------
    dict
    """
    result = {}
    
    # Get filename from path
    filename = file_path.split('/')[-1]
    
    # Check if file is an asset or rendition
    if filename.startswith(prefix):
        if '_rendition' in filename:
            result['type'] = 'rendition'
        else:
            result['type'] = 'asset'
        result['path'] = file_path
        
    return result