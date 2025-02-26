def formatmany(
                self,
                sql: AnyStr,
                many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
        ) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    # Determine the parameter style based on the input
    if isinstance(many_params, dict):
        param_style = 'named'
    elif isinstance(many_params, list) and all(isinstance(param, (list, tuple)) for param in many_params):
        param_style = 'ordinal'
    else:
        raise ValueError("Invalid parameter style. Must be a mapping or a sequence of sequences.")

    # Prepare the output parameters and formatted SQL
    out_params = []
    formatted_sql = sql

    # Iterate through each set of parameters
    for params in many_params:
        if param_style == 'named':
            if not isinstance(params, dict):
                raise ValueError("Expected a mapping for named parameter style.")
            # Replace named parameters in SQL with their corresponding values
            for key, value in params.items():
                formatted_sql = formatted_sql.replace(f":{key}", str(value))
            out_params.append(params)
        else:  # ordinal
            if not isinstance(params, (list, tuple)):
                raise ValueError("Expected a sequence for ordinal parameter style.")
            # Replace ordinal parameters in SQL with their corresponding values
            for index, value in enumerate(params):
                formatted_sql = formatted_sql.replace(f"?{index + 1}", str(value))
            out_params.append(list(params))

    return formatted_sql, out_params