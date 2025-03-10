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
        caminho completo do arquivo

    Returns
    -------
    dict
        Um dicionário contendo o tipo de arquivo e o caminho do arquivo.
    """
    import os

    # Extrai o nome do arquivo e a extensão
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1].lower()

    # Determina o tipo de arquivo com base na extensão
    if file_extension in ['.jpg', '.png', '.gif', '.mp4', '.mov']:
        file_type = 'asset'
    elif file_extension in ['.xml', '.json', '.txt']:
        file_type = 'rendition'
    else:
        file_type = 'unknown'

    # Retorna um dicionário com o tipo de arquivo e o caminho do arquivo
    return {
        'type': file_type,
        'path': file_path
    }