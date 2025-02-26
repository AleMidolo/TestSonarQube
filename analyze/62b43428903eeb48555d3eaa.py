def formatmany(
                self,
                sql: AnyStr,
                many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
        ) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    # Convert the SQL query to use "out" style parameters
    out_params = []
    param_count = 0

    # Determine the parameter style
    if isinstance(many_params, dict):
        for params in many_params:
            if isinstance(params, dict):
                out_params.append({k: v for k, v in params.items()})
                param_count += len(params)
            elif isinstance(params, (list, tuple)):
                out_params.append(list(params))
                param_count += len(params)
    else:
        for params in many_params:
            if isinstance(params, dict):
                out_params.append({k: v for k, v in params.items()})
                param_count += len(params)
            elif isinstance(params, (list, tuple)):
                out_params.append(list(params))
                param_count += len(params)

    # Replace the parameters in the SQL query
    formatted_sql = sql
    for i in range(param_count):
        formatted_sql = formatted_sql.replace(f'${i + 1}', f':param{i + 1}')

    return formatted_sql, out_params