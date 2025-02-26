def formatmany(
                self,
                sql: AnyStr,
                many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
        ) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    # Determine the parameter style based on the input
    if isinstance(many_params, dict):
        # Named parameter style
        param_style = 'named'
    elif isinstance(many_params, list) and all(isinstance(param, (list, tuple)) for param in many_params):
        # Ordinal parameter style
        param_style = 'ordinal'
    else:
        raise ValueError("Invalid parameter style. Must be a mapping or a sequence of sequences.")

    # Prepare the formatted SQL and the list of converted parameters
    formatted_sql = sql
    converted_params = []

    for params in many_params:
        if param_style == 'named':
            if not isinstance(params, dict):
                raise ValueError("Expected a mapping for named parameter style.")
            # Convert named parameters to out-style
            converted_param = {f":{key}": value for key, value in params.items()}
            converted_params.append(converted_param)
            # Replace named parameters in SQL
            for key in params.keys():
                formatted_sql = formatted_sql.replace(f":{key}", f"%({key})s")
        else:
            if not isinstance(params, (list, tuple)):
                raise ValueError("Expected a sequence for ordinal parameter style.")
            # Convert ordinal parameters to out-style
            converted_param = list(params)
            converted_params.append(converted_param)
            # Replace ordinal parameters in SQL
            for index in range(len(params)):
                formatted_sql = formatted_sql.replace(f"?", f"%s", 1)

    return formatted_sql, converted_params