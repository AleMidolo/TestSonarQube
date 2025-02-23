def format(
                self,
                sql: AnyStr,
                params: Union[Dict[Union[str, int], Any], Sequence[Any]],
        ) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    Convierte la consulta SQL para usar parámetros de estilo "out" en lugar de parámetros de estilo "in".

    *sql* (:class:`str` o :class:`bytes`) es la consulta SQL.

    *params* (:class:`~collections.abc.Mapping` o :class:`~collections.abc.Sequence`)  
    contiene el conjunto de parámetros de estilo "in". Mapea cada parámetro  
    (:class:`str` o :class:`int`) a un valor. Si :attr:`.SQLParams.in_style`  
    es un estilo de parámetro con nombre, entonces *params* debe ser un :class:`~collections.abc.Mapping`.  
    Si :attr:`.SQLParams.in_style` es un estilo de parámetro ordinal, entonces  
    *params* debe ser un :class:`~collections.abc.Sequence`.

    Devuelve una :class:`tuple` que contiene:

    - La consulta SQL formateada (:class:`str` o :class:`bytes`).

    - El conjunto de parámetros convertidos de estilo "out" (:class:`dict` o  
      :class:`list`).
    """
    # Implementación del método
    if isinstance(params, dict):
        # Convertir parámetros de estilo "in" a estilo "out" para un diccionario
        out_params = {key: params[key] for key in params}
        formatted_sql = sql
        for key in out_params:
            formatted_sql = formatted_sql.replace(f":{key}", f"${key}")
    elif isinstance(params, (list, tuple)):
        # Convertir parámetros de estilo "in" a estilo "out" para una secuencia
        out_params = list(params)
        formatted_sql = sql
        for index in range(len(out_params)):
            formatted_sql = formatted_sql.replace(f"?{index}", f"${index + 1}")
    else:
        raise ValueError("params must be a dictionary or a sequence")

    return formatted_sql, out_params