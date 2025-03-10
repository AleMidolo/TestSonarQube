def format(
        self,
        sql: AnyStr,
        params: Union[Dict[Union[str, int], Any], Sequence[Any]],
) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    Converte la query SQL per utilizzare i parametri in stile "out" invece dei parametri in stile "in".

    **sql** (:class:`str` o :class:`bytes`) è la query SQL.

    Restituisce una :class:`tuple` contenente:
    - La query SQL formattata (:class:`str` o :class:`bytes`).
    - L'insieme dei parametri convertiti in stile "out" (:class:`dict` o :class:`list`).
    """
    if isinstance(params, dict):
        # Convert dictionary params to out style
        out_params = {f"out_{key}": value for key, value in params.items()}
        # Replace placeholders in SQL with out style placeholders
        formatted_sql = sql
        for key in params.keys():
            formatted_sql = formatted_sql.replace(f":{key}", f":out_{key}")
    elif isinstance(params, (list, tuple)):
        # Convert list/tuple params to out style
        out_params = [f"out_{i}" for i in range(len(params))]
        # Replace placeholders in SQL with out style placeholders
        formatted_sql = sql
        for i in range(len(params)):
            formatted_sql = formatted_sql.replace(f"?", f":out_{i}", 1)
    else:
        raise TypeError("params must be a dict, list, or tuple")

    return formatted_sql, out_params