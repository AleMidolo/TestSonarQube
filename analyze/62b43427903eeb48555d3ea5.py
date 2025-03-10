def format(
        self,
        sql: AnyStr,
        params: Union[Dict[Union[str, int], Any], Sequence[Any]],
) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    Convert the SQL query to use the out-style parameters instead of
    the in-style parameters.

    *sql* (:class:`str` or :class:`bytes`) is the SQL query.

    *params* (:class:`~collections.abc.Mapping` or :class:`~collections.abc.Sequence`)
    contains the set of in-style parameters. It maps each parameter
    (:class:`str` or :class:`int`) to value. If :attr:`.SQLParams.in_style`
    is a named parameter style. then *params* must be a :class:`~collections.abc.Mapping`.
    If :attr:`.SQLParams.in_style` is an ordinal parameter style, then
    *params* must be a :class:`~collections.abc.Sequence`.

    Returns a :class:`tuple` containing:

    -       The formatted SQL query (:class:`str` or :class:`bytes`).

    -       The set of converted out-style parameters (:class:`dict` or
            :class:`list`).
    """
    if isinstance(params, dict):
        # Named parameter style
        out_params = {}
        for key, value in params.items():
            out_params[f":{key}"] = value
        formatted_sql = sql
        for key, value in params.items():
            formatted_sql = formatted_sql.replace(f":{key}", f"?")
        return formatted_sql, out_params
    elif isinstance(params, (list, tuple)):
        # Ordinal parameter style
        out_params = list(params)
        formatted_sql = sql
        for i in range(len(params)):
            formatted_sql = formatted_sql.replace(f"?", f":{i+1}", 1)
        return formatted_sql, out_params
    else:
        raise TypeError("params must be a Mapping or Sequence")