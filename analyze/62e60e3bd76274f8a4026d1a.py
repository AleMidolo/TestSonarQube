def from_raw_values(cls, values):
    """
    Crea un oggetto Bookmarks da una lista di valori stringa grezzi dei segnalibri.

    Non dovresti aver bisogno di utilizzare questo metodo a meno che tu non voglia
    deserializzare i segnalibri.

    :param values: Valori stringa ASCII (segnalibri grezzi)
    :type values: Iterable[str]
    """
    bookmarks = []
    for value in values:
        try:
            # Rimuove eventuali spazi bianchi e converte in stringa
            bookmark = str(value).strip()
            if bookmark:  # Verifica che non sia vuoto
                bookmarks.append(bookmark)
        except (ValueError, TypeError):
            continue
            
    return cls(bookmarks)