def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    """
    Convert the SQL query to use the out-style parameters instead of the
    in-style parameters.

    *sql* (:class:`str` or :class:`bytes`) is the SQL query.

    *many_params* (:class:`~collections.abc.Iterable`) contains each set
    of in-style parameters (*params*).

    -       *params* (:class:`~collections.abc.Mapping` or :class:`~collections.abc.Sequence`)
            contains the set of in-style parameters. It maps each parameter
            (:class:`str` or :class:`int`) to value. If :attr:`.SQLParams.in_style`
            is a named parameter style. then *params* must be a :class:`~collections.abc.Mapping`.
            If :attr:`.SQLParams.in_style` is an ordinal parameter style. then
            *params* must be a :class:`~collections.abc.Sequence`.

    Returns a :class:`tuple` containing:

    -       The formatted SQL query (:class:`str` or :class:`bytes`).

    -       A :class:`list` containing each set of converted out-style
            parameters (:class:`dict` or :class:`list`).
    """
    # Convert each set of parameters
    out_params_list = []
    for params in many_params:
        # Format single set of parameters
        _, out_params = self.format(sql, params)
        out_params_list.append(out_params)

    # Format SQL query once with first set of parameters
    # This ensures SQL is formatted consistently
    formatted_sql, _ = self.format(sql, next(iter(many_params)))
    
    return formatted_sql, out_params_list