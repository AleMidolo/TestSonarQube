def dict_insert(dic, val, key, *keys):
    """
    Inserisce un valore in una chiave annidata all'interno di un dizionario.

    Per inserire un valore in una chiave annidata, è necessario fornire tutte le chiavi antenate
    come argomenti del metodo.

    Esempio:
      dict_insert({}, 'val', *'key1.key2'.split('.'))

    :param dic: un oggetto dizionario in cui inserire il valore della chiave annidata
    :param val: un valore da inserire nel dizionario fornito
    :param key: la prima chiave nella catena di chiavi che conterrà il valore
    :param keys: sottochiavi nella catena di chiavi
    """
    current = dic
    for k in keys[:-1]:
        if k not in current:
            current[k] = {}
        current = current[k]
    current[keys[-1] if keys else key] = val