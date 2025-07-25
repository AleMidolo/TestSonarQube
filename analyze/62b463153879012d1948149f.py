def _eval_file(prefix, file_path):
    """
    Identifica o tipo de arquivo do pacote: `asset` ou `rendition`.

    Identifica o tipo de arquivo do pacote e atualiza `packages` com o tipo e
    o endere��o do arquivo em an��lise.

    Parameters
    ----------
    prefix : str
        nome do arquivo XML sem extens��o
    filename : str
        filename
    file_folder : str
        file folder

    Returns
    -------
    dict
    """
    result = {}
    
    # Check if file path contains rendition or asset
    if 'rendition' in file_path.lower():
        result[prefix] = {
            'type': 'rendition',
            'path': file_path
        }
    else:
        result[prefix] = {
            'type': 'asset', 
            'path': file_path
        }
        
    return result