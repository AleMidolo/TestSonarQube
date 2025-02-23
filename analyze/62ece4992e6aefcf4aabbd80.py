def remove_ending_os_sep(input_list):
    """
    Itera su un elenco di stringhe e rimuovi i caratteri separatori di sistema operativi (os) finali.

    Ogni stringa viene verificata per controllare se la sua lunghezza è maggiore di uno e se l'ultimo
    carattere è il separatore di percorso. In tal caso, il carattere separatore di percorso
    viene rimosso.

    Argomenti:
        input_list: elenco di stringhe

    Restituisce:
        Elenco elaborato di stringhe

    Eccezioni:
        TypeError
    """
    import os

    if not isinstance(input_list, list):
        raise TypeError("input_list deve essere un elenco di stringhe")

    processed_list = []
    for item in input_list:
        if not isinstance(item, str):
            raise TypeError("Tutti gli elementi in input_list devono essere stringhe")
        if len(item) > 1 and item[-1] == os.sep:
            processed_list.append(item[:-1])
        else:
            processed_list.append(item)

    return processed_list