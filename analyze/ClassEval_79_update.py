def update(self, data, condition):
    """
    Genera un'istruzione SQL UPDATE basata sui dati e sulla condizione forniti.
    :param data: dict. I dati da aggiornare, in forma di dizionario dove le chiavi sono i nomi dei campi e i valori sono i nuovi valori dei campi.
    :param condition: str. L'espressione di condizione per l'aggiornamento.
    :return: str. L'istruzione SQL generata.
    >>> sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
    "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
    """
    set_clauses = []
    for field, value in data.items():
        if isinstance(value, str):
            set_clauses.append(f"{field} = '{value}'")
        else:
            set_clauses.append(f"{field} = {value}")
    
    set_statement = ", ".join(set_clauses)
    sql_query = f"UPDATE {self.table} SET {set_statement} WHERE {condition};"
    
    return sql_query