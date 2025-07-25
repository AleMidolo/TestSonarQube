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
            # Replace named parameters in the SQL
            for key, value in params.items():
                formatted_sql = formatted_sql.replace(f":{key}", str(value))
            converted_params.append(params)
        elif param_style == 'ordinal':
            if not isinstance(params, (list, tuple)):
                raise ValueError("Expected a sequence for ordinal parameter style.")
            # Replace ordinal parameters in the SQL
            for index, value in enumerate(params):
                formatted_sql = formatted_sql.replace(f"?{index + 1}", str(value))
            converted_params.append(params)

    return formatted_sql, converted_params