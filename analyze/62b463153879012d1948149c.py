def select_filenames_by_prefix(prefix, files):
    """
    Get files which belongs to a document package.

    Retorna os arquivos da lista `files` cujos nomes iniciam com `prefix`

    Parameters
    ----------
    prefix : str
        Filename prefix
    files : str list
        Files paths
    Returns
    -------
    list
        files paths which basename files matches to prefix
    """
    from os.path import basename
    
    return [file for file in files if basename(file).startswith(prefix)]