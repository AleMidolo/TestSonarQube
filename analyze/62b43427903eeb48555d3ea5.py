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
    # Determine if the SQLParams.in_style is named or ordinal
    if isinstance(params, dict):  # Named parameters
        out_params = {}
        for key, value in params.items():
            out_key = f":{key}"  # Convert to out-style parameter
            out_params[out_key] = value
        formatted_sql = sql
        for key in params.keys():
            formatted_sql = formatted_sql.replace(f":{key}", f"{out_key}")
    elif isinstance(params, (list, tuple)):  # Ordinal parameters
        out_params = list(params)
        formatted_sql = sql
        for index in range(len(params)):
            formatted_sql = formatted_sql.replace(f"?", f"{out_params[index]}", 1)
    else:
        raise ValueError("params must be a dictionary or a sequence")

    return formatted_sql, out_params