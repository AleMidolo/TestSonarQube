def format(
        self,
        sql: AnyStr,
        params: Union[Dict[Union[str, int], Any], Sequence[Any]],
) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    Convierte la consulta SQL para usar parámetros de estilo "out" en lugar de parámetros de estilo "in".

    Args:
        sql (AnyStr): La consulta SQL.
        params (Union[Dict[Union[str, int], Any], Sequence[Any]]): Los parámetros de estilo "in".

    Returns:
        Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]: Una tupla con la consulta SQL formateada y los parámetros convertidos.
    """
    if isinstance(params, dict):
        # Convertir parámetros nombrados
        out_params = {}
        for key, value in params.items():
            out_key = f":{key}" if isinstance(key, str) else f":param{key}"
            out_params[out_key] = value
        formatted_sql = sql
    elif isinstance(params, (list, tuple)):
        # Convertir parámetros ordinales
        out_params = []
        for i, value in enumerate(params):
            out_params.append(value)
        formatted_sql = sql
    else:
        raise TypeError("params debe ser un diccionario o una secuencia")

    return formatted_sql, out_params