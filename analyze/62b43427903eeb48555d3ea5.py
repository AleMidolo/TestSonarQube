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
                out_params[key] = value
        return sql, out_params
    elif isinstance(params, (list, tuple)):
        # Convert positional parameters to out-style
        out_params = list(params)
        return sql, out_params
    else:
        raise TypeError("params must be a dict, list, or tuple")