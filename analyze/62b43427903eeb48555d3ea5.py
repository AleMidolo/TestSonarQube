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
                formatted_sql = formatted_sql.replace(f"%({key})s", f":{key}")
            else:
                formatted_sql = formatted_sql.replace(f"%s", f":{key}", 1)
        return formatted_sql, out_params
    elif isinstance(params, (list, tuple)):
        # Convert positional parameters to out-style
        out_params = {}
        formatted_sql = sql
        for i, value in enumerate(params):
            param_name = f":param{i}"
            out_params[param_name] = value
            formatted_sql = formatted_sql.replace("%s", param_name, 1)
        return formatted_sql, out_params
    else:
        raise TypeError("params must be a dict, list, or tuple")