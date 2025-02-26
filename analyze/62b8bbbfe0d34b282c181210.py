def append_text_to_file(file_name, text_buffer, encoding, overwrite=False):
    """
    Scrive nel file specificato il buffer di testo fornito.  
    Crea il file se necessario.  
    :param file_name: Nome del file.  
    :type file_name: str  
    :param text_buffer: Buffer di testo da scrivere.  
    :type text_buffer: str  
    :param encoding: La codifica da utilizzare.  
    :type encoding: str  
    :param overwrite: Se impostato a True, il file viene sovrascritto.  
    :type overwrite: bool  
    :return: Il numero di byte scritti o un valore inferiore a 0 in caso di errore.  
    :rtype int  
    """
    try:
        mode = 'w' if overwrite else 'a'
        with open(file_name, mode, encoding=encoding) as file:
            bytes_written = file.write(text_buffer)
            return bytes_written
    except Exception as e:
        return -1