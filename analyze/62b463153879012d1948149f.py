import os

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
    file_name = os.path.basename(file_path)
    file_folder = os.path.dirname(file_path)
    
    if prefix in file_name:
        if "asset" in file_name.lower():
            file_type = "asset"
        elif "rendition" in file_name.lower():
            file_type = "rendition"
        else:
            file_type = "unknown"
    else:
        file_type = "unknown"
    
    return {
        "type": file_type,
        "path": file_path,
        "folder": file_folder
    }