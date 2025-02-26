def _eval_file(prefix, file_path):
    """
    Identifica o tipo de arquivo do pacote: `asset` ou `rendition`.

    Identifica o tipo de arquivo do pacote e atualiza `packages` com o tipo e
    o endereço do arquivo em análise.

    Parameters
    ----------
    prefix : str
        nome do arquivo XML sem extensão
    file_path : str
        caminho do arquivo

    Returns
    -------
    dict
    """
    import os

    # Initialize the result dictionary
    result = {}

    # Extract the file name and extension
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))

    # Determine the type of file based on its extension
    if file_extension in ['.xml', '.json']:
        file_type = 'asset'
    elif file_extension in ['.jpg', '.png', '.gif']:
        file_type = 'rendition'
    else:
        file_type = 'unknown'

    # Update the result dictionary
    result['prefix'] = prefix
    result['file_type'] = file_type
    result['file_path'] = file_path

    return result