def update(self, data, condition):
    """
    Genera un'istruzione SQL UPDATE basata sui dati e sulla condizione forniti.
    :param data: dict. I dati da aggiornare, in forma di dizionario dove le chiavi sono i nomi dei campi e i valori sono i nuovi valori dei campi.
    :param condition: str. L'espressione di condizione per l'aggiornamento.
    :return: str. L'istruzione SQL generata.
    >>> sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
    "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
    """
    # Costruisce la parte SET dell'istruzione SQL
    set_parts = []
    for field, value in data.items():
        # Aggiunge le virgolette ai valori stringa
        if isinstance(value, str):
            set_parts.append(f"{field} = '{value}'")
        else:
            set_parts.append(f"{field} = {value}")
    
    set_clause = ", ".join(set_parts)
    
    # Costruisce l'istruzione SQL completa
    # Assumendo che self abbia un attributo 'table' che contiene il nome della tabella
    sql_statement = f"UPDATE {self.table} SET {set_clause} WHERE {condition};"
    
    return sql_statement