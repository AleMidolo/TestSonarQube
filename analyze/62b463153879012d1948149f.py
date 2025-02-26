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

    # Extract the file extension
    _, file_extension = os.path.splitext(file_path)

    # Determine the type of file based on the extension
    if file_extension in ['.jpg', '.png', '.gif']:
        result['type'] = 'asset'
    elif file_extension in ['.mp4', '.mov', '.avi']:
        result['type'] = 'rendition'
    else:
        result['type'] = 'unknown'

    # Update the result with the prefix and file path
    result['prefix'] = prefix
    result['file_path'] = file_path

    return result