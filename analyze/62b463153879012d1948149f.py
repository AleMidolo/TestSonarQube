def _eval_file(prefix, file_path):
    """
    Identifica el tipo de archivo del paquete: `asset` o `rendition`.

    Identifica el tipo de archivo del paquete y actualiza `packages` con el tipo y
    la ruta del archivo en análisis.

    Parámetros
    ----------
    prefix : str
        nombre del archivo XML sin extensión
    file_path : str
        ruta completa del archivo

    Retorna
    -------
    dict
        Un diccionario con el tipo de archivo y la ruta del archivo.
    """
    import os

    # Extraer el nombre del archivo y la extensión
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1].lower()

    # Determinar el tipo de archivo basado en la extensión
    if file_extension in ['.jpg', '.png', '.gif', '.tiff', '.bmp']:
        file_type = 'asset'
    elif file_extension in ['.mp4', '.mov', '.avi', '.mkv']:
        file_type = 'rendition'
    else:
        file_type = 'unknown'

    # Crear el diccionario de retorno
    result = {
        'prefix': prefix,
        'file_path': file_path,
        'file_type': file_type
    }

    return result