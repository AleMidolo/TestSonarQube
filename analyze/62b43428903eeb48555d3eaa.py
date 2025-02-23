def formatmany(
                self,
                sql: AnyStr,
                many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
        ) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    # Convert the SQL query to use "out" style parameters
    out_params = []
    param_count = 0

    # Determine the parameter style
    for params in many_params:
        if isinstance(params, dict):
            out_param = {key: f'${param_count + i + 1}' for i, (key, value) in enumerate(params.items())}
            out_params.append(out_param)
        elif isinstance(params, (list, tuple)):
            out_param = [f'${param_count + i + 1}' for i in range(len(params))]
            out_params.append(out_param)
        param_count += len(params)

    # Replace the parameters in the SQL query
    formatted_sql = sql
    for i in range(param_count):
        formatted_sql = formatted_sql.replace(f'${i + 1}', f'${i + 1}')

    return formatted_sql, out_params