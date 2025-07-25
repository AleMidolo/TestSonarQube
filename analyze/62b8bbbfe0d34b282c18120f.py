def file_to_textbuffer(file_name, encoding):
    """
    Carica un file in un buffer di testo (UTF-8), utilizzando la codifica specificata durante la lettura.
    ATTENZIONE: Questo metodo leggerà l'intero file IN MEMORIA.
    :param file_name: Nome del file.
    :type file_name: str
    :param encoding: Codifica da utilizzare.
    :type encoding: str
    :return: Un buffer di testo o None in caso di errore.
    :rtype: str
    """
    try:
        with open(file_name, 'r', encoding=encoding) as file:
            text_buffer = file.read()
        return text_buffer
    except Exception as e:
        print(f"Errore durante la lettura del file: {e}")
        return None