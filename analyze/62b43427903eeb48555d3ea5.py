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
    # Convertir los parámetros de estilo "in" a estilo "out"
    if isinstance(params, dict):
        # Si es un diccionario, asumimos que es un estilo de parámetro con nombre
        out_params = {k: f":{k}" for k in params.keys()}
    else:
        # Si es una secuencia, asumimos que es un estilo de parámetro ordinal
        out_params = [f":{i}" for i in range(len(params))]

    # Formatear la consulta SQL
    if isinstance(sql, bytes):
        formatted_sql = sql
    else:
        formatted_sql = sql

    return formatted_sql, out_params