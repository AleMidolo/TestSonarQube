def insert(self, data):
    """
    Genera un'istruzione SQL INSERT basata sui dati forniti.
    :param data: dict. I dati da inserire, in forma di dizionario dove le chiavi sono i nomi dei campi e i valori sono i valori dei campi.
    :return: str. L'istruzione SQL generata.
    >>> sql.insert({'key1': 'value1', 'key2': 'value2'})
    "INSERT INTO table1 (key1, key2) VALUES ('value1', 'value2');"
    """
    if not data:
        return ""
    
    # Estrai le chiavi (nomi dei campi) e i valori
    columns = ', '.join(data.keys())
    
    # Formatta i valori: aggiungi apici singoli per le stringhe
    values = ', '.join(f"'{value}'" if isinstance(value, str) else str(value) for value in data.values())
    
    # Costruisci l'istruzione SQL INSERT
    # Assumendo che self abbia un attributo table_name (es. 'table1' dall'esempio)
    table_name = getattr(self, 'table_name', 'table1')
    
    return f"INSERT INTO {table_name} ({columns}) VALUES ({values});"