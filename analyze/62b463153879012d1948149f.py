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
        Um dicionário contendo o tipo de arquivo ('asset' ou 'rendition') e o caminho do arquivo.
    """
    # Verifica se o arquivo é um asset ou rendition baseado no prefixo
    if prefix.startswith("asset"):
        file_type = "asset"
    elif prefix.startswith("rendition"):
        file_type = "rendition"
    else:
        file_type = "unknown"

    # Retorna um dicionário com o tipo de arquivo e o caminho do arquivo
    return {
        "type": file_type,
        "file_path": file_path
    }