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
    # Determine if the parameters are in a mapping or sequence
    if isinstance(params, dict):
        # Named parameters
        out_params = {}
        for key, value in params.items():
            out_params[key] = value
            sql = sql.replace(f":{key}", "?")
    elif isinstance(params, (list, tuple)):
        # Ordinal parameters
        out_params = list(params)
        for index in range(len(params)):
            sql = sql.replace(f"${index + 1}", "?")
    else:
        raise TypeError("params must be a dict or a sequence")

    return sql, out_params