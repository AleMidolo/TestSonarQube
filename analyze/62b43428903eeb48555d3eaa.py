def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    formatted_sql = sql
    formatted_params = []

    for params in many_params:
        if isinstance(params, dict):
            # Convert named parameters to out style
            out_params = {f":{key}": value for key, value in params.items()}
        elif isinstance(params, (list, tuple)):
            # Convert ordinal parameters to out style
            out_params = [f":{i}" for i in range(len(params))]
        else:
            raise TypeError("params must be a dict, list, or tuple")

        formatted_params.append(out_params)

    return formatted_sql, formatted_params