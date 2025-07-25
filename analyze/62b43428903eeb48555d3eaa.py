def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    """
    Convierte la consulta SQL para usar parámetros de estilo "out" en lugar de parámetros de estilo "in".

    *sql*(:class:`str` o :class:`bytes`) es la consulta SQL.

    *many_params* (:class:`~collections.abc.Iterable`) contiene cada conjunto de parámetros de estilo "in" (*params*).

      - *params* (:class:`~collections.abc.Mapping` o :class:`~collections.abc.Sequence`) contiene el conjunto de parámetros de estilo "in". Mapea cada parámetro (:class:`str` o :class:`int`) a un valor. Si :attr:`.SQLParams.in_style` es un estilo de parámetro nombrado, entonces *params* debe ser un :class:`~collections.abc.Mapping`. Si :attr:`.SQLParams.in_style` es un estilo de parámetro ordinal, entonces *params* debe ser un :class:`~collections.abc.Sequence`.

    Devuelve una :class:`tuple` que contiene:

    - La consulta SQL formateada (:class:`str` o :class:`bytes`).

    - Una :class:`list` que contiene cada conjunto de parámetros convertidos de estilo "out" (:class:`dict` o :class:`list`).
    """
    formatted_sql = sql
    formatted_params = []

    for params in many_params:
        if isinstance(params, dict):
            # Convertir parámetros nombrados a estilo "out"
            out_params = {k: f":{k}" for k in params.keys()}
        elif isinstance(params, (list, tuple)):
            # Convertir parámetros ordinales a estilo "out"
            out_params = [f":{i}" for i in range(len(params))]
        else:
            raise TypeError("Los parámetros deben ser un diccionario o una secuencia.")

        formatted_params.append(out_params)

    return formatted_sql, formatted_params