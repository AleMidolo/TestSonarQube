def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]:
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
    formatted_sql = sql
    formatted_params = []

    for params in many_params:
        if isinstance(params, dict):
            # Handle named parameters
            formatted_params.append({k: v for k, v in params.items()})
        elif isinstance(params, (list, tuple)):
            # Handle ordinal parameters
            formatted_params.append(list(params))
        else:
            raise TypeError("params must be a Mapping or Sequence")

    return formatted_sql, formatted_params