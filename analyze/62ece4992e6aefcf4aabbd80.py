import os

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
    if not isinstance(input_list, list):
        raise TypeError("L'argomento deve essere una lista di stringhe.")
    
    processed_list = []
    for string in input_list:
        if not isinstance(string, str):
            raise TypeError("Tutti gli elementi della lista devono essere stringhe.")
        
        if len(string) > 1 and string[-1] == os.sep:
            processed_list.append(string[:-1])
        else:
            processed_list.append(string)
    
    return processed_list