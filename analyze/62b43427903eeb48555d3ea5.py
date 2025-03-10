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
        # Convert dictionary-style params to out-style
        out_params = {k: f":{k}" for k in params.keys()}
        formatted_sql = sql
        for key, value in params.items():
            formatted_sql = formatted_sql.replace(f":{key}", f":{key}_out")
        return formatted_sql, out_params
    elif isinstance(params, (list, tuple)):
        # Convert list-style params to out-style
        out_params = [f":{i}" for i in range(len(params))]
        formatted_sql = sql
        for i in range(len(params)):
            formatted_sql = formatted_sql.replace("?", f":{i}_out", 1)
        return formatted_sql, out_params
    else:
        raise TypeError("params must be either a dict, list, or tuple")