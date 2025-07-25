def format(
        self,
        sql: AnyStr,
        params: Union[Dict[Union[str, int], Any], Sequence[Any]],
) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    if isinstance(params, dict):
        # Convert named parameters to out-style
        out_params = {}
        for key, value in params.items():
            if isinstance(key, str):
                out_params[f":{key}"] = value
            else:
                out_params[f":{key}"] = value
        formatted_sql = sql
        for key, value in params.items():
            if isinstance(key, str):
                formatted_sql = formatted_sql.replace(f":{key}", "?")
            else:
                formatted_sql = formatted_sql.replace(f":{key}", "?")
        return formatted_sql, list(out_params.values())
    elif isinstance(params, (list, tuple)):
        # Convert positional parameters to out-style
        formatted_sql = sql
        for i in range(len(params)):
            formatted_sql = formatted_sql.replace(f":{i}", "?")
        return formatted_sql, list(params)
    else:
        raise TypeError("params must be a dict, list, or tuple")