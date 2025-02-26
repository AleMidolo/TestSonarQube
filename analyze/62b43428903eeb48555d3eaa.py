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
                out_params.append({key: params[key] for key in params})
            elif isinstance(params, (list, tuple)):
                out_params.append(list(params))
            param_count += 1
    else:
        for params in many_params:
            if isinstance(params, dict):
                out_params.append({key: params[key] for key in params})
            elif isinstance(params, (list, tuple)):
                out_params.append(list(params))
            param_count += 1

    # Replace "in" style parameters in the SQL with "out" style
    formatted_sql = sql
    for i in range(param_count):
        formatted_sql = formatted_sql.replace(f'{{{i}}}', f'${i + 1}')

    return formatted_sql, out_params