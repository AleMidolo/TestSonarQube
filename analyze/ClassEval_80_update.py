@staticmethod
def update(table, data, where=None):
    """
    Genera la declaración SQL UPDATE a partir de los parámetros dados.
    :param table: str, la tabla que se ejecutará con la operación UPDATE en la base de datos
    :param data: dict, la clave y el valor en la declaración SQL de actualización
    :param where: dict, {key1: value1, key2: value2 ...}. La condición de la consulta.
    >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
    "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
    """
    # Construir la parte SET de la consulta
    set_parts = []
    for key, value in data.items():
        if isinstance(value, str):
            set_parts.append(f"{key}='{value}'")
        else:
            set_parts.append(f"{key}='{value}'")
    
    set_clause = ", ".join(set_parts)
    
    # Construir la consulta base
    query = f"UPDATE {table} SET {set_clause}"
    
    # Agregar la cláusula WHERE si existe
    if where:
        where_parts = []
        for key, value in where.items():
            if isinstance(value, str):
                where_parts.append(f"{key}='{value}'")
            else:
                where_parts.append(f"{key}='{value}'")
        
        where_clause = " AND ".join(where_parts)
        query += f" WHERE {where_clause}"
    
    return query