def format(
    self,
    sql: AnyStr,
    params: Union[Dict[Union[str, int], Any], Sequence[Any]],
) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    Converte la query SQL per utilizzare i parametri in stile "out" invece dei parametri in stile "in".

    Args:
        sql (AnyStr): La query SQL.
        params (Union[Dict[Union[str, int], Any], Sequence[Any]]): I parametri da convertire.

    Returns:
        Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]: Tupla contenente la query SQL formattata
        e l'insieme dei parametri convertiti.
    """
    # Se i parametri sono una sequenza
    if isinstance(params, (list, tuple)):
        # Converte ogni ? in %s
        formatted_sql = sql.replace('?', '%s')
        return formatted_sql, params

    # Se i parametri sono un dizionario
    elif isinstance(params, dict):
        # Converte ogni :name o @name in %(name)s
        formatted_sql = sql
        for key in params.keys():
            formatted_sql = formatted_sql.replace(f':{key}', f'%({key})s')
            formatted_sql = formatted_sql.replace(f'@{key}', f'%({key})s')
        return formatted_sql, params

    # Se i parametri non sono né sequenza né dizionario
    else:
        raise ValueError("I parametri devono essere una sequenza o un dizionario")