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
        nombre del archivo

    Retorna
    -------
    dict
    """
    import os

    # Initialize the packages dictionary
    packages = {}

    # Get the file extension
    _, file_extension = os.path.splitext(file_path)

    # Determine the type of file based on the extension
    if file_extension in ['.jpg', '.png', '.gif']:
        file_type = 'asset'
    elif file_extension in ['.mp4', '.mov', '.avi']:
        file_type = 'rendition'
    else:
        file_type = 'unknown'

    # Update the packages dictionary
    packages[prefix] = {
        'type': file_type,
        'path': file_path
    }

    return packages