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

    # Prepare the formatted SQL and the converted parameters
    formatted_sql = sql
    converted_params = []

    for params in many_params:
        if param_style == 'named':
            if not isinstance(params, dict):
                raise ValueError("Expected a mapping for named parameter style.")
            # Replace named parameters in the SQL with placeholders
            for key, value in params.items():
                placeholder = f":{key}"
                formatted_sql = formatted_sql.replace(placeholder, str(value))
            converted_params.append(params)
        elif param_style == 'ordinal':
            if not isinstance(params, (list, tuple)):
                raise ValueError("Expected a sequence for ordinal parameter style.")
            # Replace ordinal parameters in the SQL with placeholders
            for index, value in enumerate(params):
                placeholder = f"${index + 1}"
                formatted_sql = formatted_sql.replace(placeholder, str(value))
            converted_params.append(list(params))

    return formatted_sql, converted_params