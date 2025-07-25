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
    
    if file_name.startswith(prefix) and file_name.endswith('.xml'):
        file_type = 'asset'
    else:
        file_type = 'rendition'
    
    return {
        'type': file_type,
        'path': file_path
    }