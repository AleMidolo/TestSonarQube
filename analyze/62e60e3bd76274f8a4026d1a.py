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
        # Supponiamo che ogni valore sia una stringa formattata come "nome:url"
        name, url = value.split(':', 1)
        bookmarks.append({'name': name.strip(), 'url': url.strip()})
    return cls(bookmarks)