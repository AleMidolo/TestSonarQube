def format(
        self,
        sql: AnyStr,
        params: Union[Dict[Union[str, int], Any], Sequence[Any]],
) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    Convierte la consulta SQL para usar parámetros de estilo "out" en lugar de parámetros de estilo "in".

    Args:
        sql: La consulta SQL como str o bytes.
        params: Los parámetros de estilo "in" como un diccionario o una secuencia.

    Returns:
        Una tupla que contiene la consulta SQL formateada y los parámetros convertidos de estilo "out".
    """
    if isinstance(params, dict):
        # Convertir parámetros de estilo "in" con nombre a estilo "out"
        out_params = {f"out_{key}": value for key, value in params.items()}
        formatted_sql = sql
        for key, value in params.items():
            formatted_sql = formatted_sql.replace(f":{key}", f":out_{key}")
    elif isinstance(params, (list, tuple)):
        # Convertir parámetros de estilo "in" ordinales a estilo "out"
        out_params = [f"out_{i}" for i in range(len(params))]
        formatted_sql = sql
        for i in range(len(params)):
            formatted_sql = formatted_sql.replace(f"?", f":out_{i}", 1)
    else:
        raise TypeError("params debe ser un diccionario o una secuencia")

    return formatted_sql, out_params